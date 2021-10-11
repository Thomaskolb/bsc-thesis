# Thomas Kolb s1027332
# This program generates pairs of captions and wav files that can be used for training

# TODO enkele captions eruit filteren
#      X-telefoonnummers
#      X-alles hoofdletters
# TODO subtitles aanpassen
#      X-getallen naar nummers
# TODO 3e argument van outputlist

# interpunctie vast aan woorden probleem

from num2words import num2words
import webvttparser
import wave
import sys
import os
import re

interpunction = ['.', ',', '!', '?']
forbidden_formats = ['.{1,}\-.{1,}', '[A-Z]{1,}\:', '[0-9]{1,}\.', '.{0,}�.{0,}']

# Function that creates the same folders as found in the datapath directory
def create_directories(datapath, outputpath):
    for folder in os.listdir(datapath):
        try:
            os.makedirs(f'{outputpath}/{folder}')
        except FileExistsError:
            pass

# Function that traverses list of datafiles and creates sample subtitle pairs
def generate_pairlist(listpath, datapath, outputpath):
    with open(listpath, 'r') as data, open(f'{outputpath}/pairlist.txt', 'w') as pairlist:
        datalist = data.read().split('\n')
        filepaths = datalist[1:len(datalist)-1]
        for filepath in filepaths:
            file_id = 0
            generate_pairs(f'{datapath}/{filepath}', outputpath, filepath, file_id, pairlist)

# Function that generates pairs for a single file
def generate_pairs(filepath, outputpath, folder, file_id, pairlist):
    captions = webvttparser.read(f'{filepath}.webm.vtt')
    try:
        os.makedirs(f'{outputpath}/{folder}')
    except:
        pass
    with wave.open(f'{filepath}.wav', 'r') as wavfile:
        for caption in captions:
            new_caption_text = acceptable_caption_text(caption.text)
            if len(new_caption_text) > 0:
                start_frame = int(webvttparser.get_time_in_seconds(caption.start) * wavfile.getframerate())
                end_frame = int(webvttparser.get_time_in_seconds(caption.end) * wavfile.getframerate())
                wavfile.setpos(start_frame)
                sampleframes = wavfile.readframes(end_frame-start_frame)
                samplepath = generate_sample(sampleframes, wavfile.getnchannels(), wavfile.getsampwidth(), 
                    wavfile.getframerate(), outputpath, folder, file_id)
                file_id = file_id + 1
                pairlist.write('{"' + new_caption_text + '", "' + samplepath + '"}\n')

# Function that filters out captions that don't match requirements
# If it is acceptable it will return an edited caption text
def acceptable_caption_text(caption_text):
    word_list = caption_text.split(' ')
    new_caption_text = ''
    for word in word_list:
        # filter for all upper letters and 'phonenumber' format 
        if word.isupper() or any([re.match(exp, word) for exp in forbidden_formats]):
            return ''
        try:
            num = int(word)
            new_caption_text += num2words(num, lang='nl') + ' '
        except:
            new_caption_text += word + ' '
    return new_caption_text[:len(new_caption_text)-1].capitalize()

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

if len(sys.argv) < 4:
    print("Please enter the path of the listed data, the data location, and the output path.")
else:
    # List of pairs of subtitles and .wav files
    # create_directories(sys.argv[2], sys.argv[3])
    generate_pairlist(sys.argv[1], sys.argv[2], sys.argv[3])
    # print(re.match('([0-9]{2})\:([0-9]{2})\:([0-9]{2}\.[0-9]{3})$', '00:00:27.039').groups())
    # samplepairs, percentage = generate_samples(sys.argv[1])