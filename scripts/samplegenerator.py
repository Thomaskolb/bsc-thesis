# Thomas Kolb s1027332
# This program generates pairs of captions and wav files that can be used for training

# TODO enkele captions eruit filteren
#      X-telefoonnummers
#      X-alles hoofdletters
# TODO subtitles aanpassen
#      X-getallen naar nummers
# TODO 3e argument van outputlist
# TODO filter nutteloze data

import captionparser
import worderrorrate
import webvttparser
import asrparser
import datetime
import wave
import sys
import os

# Minimum error rate allowed
min_wer = 0.5

# Amount of seconds that are subtracted from start time to compensate for subtitles being displayed too late
subtract_start_time = 0.1

# Function that creates the same folders as found in the datapath directory
def create_directories(datapath, outputpath):
    for folder in os.listdir(datapath):
        try:
            os.makedirs(f'{outputpath}/{folder}')
        except FileExistsError:
            pass

# Function that traverses list of datafiles and creates sample subtitle pairs
def generate_pairlist(listpath, datapath, outputpath, type):
    caption_count = 0
    total_caption_count = 0
    total_seconds = 0
    wer_sum = 0
    with open(listpath, 'r') as data, \
            open(f'{outputpath}/words.wrd', 'w') as wrd, \
            open(f'{outputpath}/letters.ltr', 'w') as ltr, \
            open(f'{outputpath}/{type}.tsv', 'w') as filelist:
        filelist.write(outputpath + '\n')
        datalist = data.read().split('\n')
        filepaths = datalist[len(datalist)-1]
        for filepath in filepaths:
            file_id = 0
            tcc, cc, wer, sc = generate_pairs(f'{datapath}/{filepath}', outputpath, filepath, file_id, filelist, wrd, ltr)
            total_caption_count += tcc
            caption_count += cc
            wer_sum += wer
            total_seconds += sc
    percentage = "{:.1f}".format((caption_count/total_caption_count)*100)
    print(f'{percentage}% of data salvaged\ttotal WER sum: {wer_sum}\tdata length = {str(datetime.timedelta(seconds=total_seconds))}')

# Function that generates pairs for a single file
def generate_pairs(filepath, outputpath, folder, file_id, filelist, wrd, ltr):
    captions = webvttparser.read(f'{filepath}.webm.vtt')
    wordsequence = asrparser.read(f'{filepath}.hyp')
    caption_count = 0
    seconds_count = 0
    wer_total = 0
    try:
        os.makedirs(f'{outputpath}/{folder}')
    except:
        pass
    with wave.open(f'{filepath}.wav', 'r') as wavfile:
        for caption in captions:
            new_caption_text = captionparser.acceptable_caption_text(caption.text)
            # If caption was accepted the length is > 0
            if len(new_caption_text) > 0:
                # check for the WER with the caption and the asr data to be lower than our threshold
                wer, asr_words = similar_caption_text(new_caption_text, caption.start, caption.end, wordsequence)
                if wer <= min_wer:
                    start_seconds = webvttparser.get_time_in_seconds(caption.start) - subtract_start_time
                    end_seconds = webvttparser.get_time_in_seconds(caption.end)
                    start_frame = int(start_seconds * wavfile.getframerate())
                    end_frame = int(end_seconds * wavfile.getframerate())
                    wavfile.setpos(start_frame)
                    sampleframes = wavfile.readframes(end_frame-start_frame)
                    samplepath = generate_sample(sampleframes, wavfile.getnchannels(), wavfile.getsampwidth(), 
                        wavfile.getframerate(), outputpath, folder, file_id)
                    file_id += 1
                    caption_count += 1
                    seconds_count += end_seconds - start_seconds
                    write_output_files(filelist, samplepath, sampleframes, new_caption_text, asr_words)
                wer_total += wer
    return len(captions), caption_count, wer_total, seconds_count

# Function that writes the output files
def write_output_files(filelist, samplepath, sampleframes, new_caption_text, asr_words, wrd, ltr):
    filelist.write(f'{samplepath}\t{sampleframes}\n')
    wrd.write(f'{new_caption_text}\n')
    ltr.write(f'{" ".join(list(str(new_caption_text).replace(" ", "|")))}" |\n"')

# Function that takes sampleframes and generates a new wav file
def generate_sample(sampleframes, channels, samplewidth, framerate, outputpath, folder, file_id):
    samplepath = f'{outputpath}/{folder}/{file_id}.wav'
    with wave.open(samplepath, 'w') as outfile:
        outfile.setnchannels(channels)
        outfile.setsampwidth(samplewidth)
        outfile.setframerate(framerate)
        outfile.setnframes(int(len(sampleframes) / samplewidth))
        outfile.writeframes(sampleframes)
        return samplepath

# Returns WER between the caption text and the text given by the output of the ASR within the same time frame
def similar_caption_text(new_caption_text, caption_start, caption_end, wordsequence):
    if len(new_caption_text) > 0:
        sequence = asrparser.search_sequence(wordsequence, 
            (webvttparser.get_time_in_seconds(caption_start) - subtract_start_time), webvttparser.get_time_in_seconds(caption_end))
        return worderrorrate.WER(new_caption_text.split(' '), sequence).wer(), sequence

if len(sys.argv) < 4:
    print("Please enter the path of the listed data, the data location, and the output directory.")
else:
    # Training data
    generate_pairlist(sys.argv[1].replace('\\', '/'), sys.argv[2].replace('\\', '/'), sys.argv[3].replace('\\', '/'), 'train')
    # Test data
    generate_pairlist(sys.argv[1].replace('\\', '/'), sys.argv[2].replace('\\', '/'), sys.argv[3].replace('\\', '/'), 'test')
    # Validation data
    generate_pairlist(sys.argv[1].replace('\\', '/'), sys.argv[2].replace('\\', '/'), sys.argv[3].replace('\\', '/'), 'valid')