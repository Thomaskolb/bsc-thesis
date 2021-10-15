# Thomas Kolb s1027332
# This program filters data that is not useful for training the wav2vec2 model

import webvttparser
import wave
import sys
import os
import re

subtitle_ext = '.vtt'
weblink_exceptions = ['nos.nl', 'service.npo.nl']
unfit_data_indicators = ['LIVEPROGRAMMA,', 'LIVEPROGRAMMA', 'LIVE', 'ONDERTITELD', 'ACHTERLOPEN', 'MUZIEK']
min_caption_count = 10

# Function that traverses all 'webm.vtt' files within a given directory
# and filters them based on requirements
def filter_vtt_data(path):
    filtered_paths = []
    path_count = 0
    for folder in os.listdir(path):
        vttfiles = [f for f in os.listdir(f"{path}/{folder}") if os.path.splitext(f)[1] == subtitle_ext]
        path_count += len(vttfiles)
        for vttfile in vttfiles:
            captions = webvttparser.read(f"{path}/{folder}/{vttfile}")
            wavfile = vttfile.split('.')[0] + '.wav'
            if (len(captions) >= min_caption_count and synchronized(captions, f'{path}/{folder}/{wavfile}') and
                    meets_data_requirements(captions)):
                filtered_paths.append(f"{folder}/{vttfile.split('.')[0]}")
    percentage = "{:.1f}".format((len(filtered_paths)/path_count)*100)
    return filtered_paths, percentage

# Function that decides whether data can be used
def meets_data_requirements(captions):
    for caption in [c.text.split() for c in captions]:
        for word in caption:
            if is_weblink(word) or is_livebroadcast(word):
                return False
    return True

# Function that checks whether caption times are within wavfile length
def synchronized(captions, wavpath):
    if os.path.isfile(wavpath):
        with wave.open(wavpath, 'r') as wavfile:
            # I also tried this for end_frame, but hardly any data was salvaged (< 3%)
            start_frame = int(webvttparser.get_time_in_seconds(captions[len(captions)-1].start) * wavfile.getframerate())
            return start_frame <= wavfile.getnframes()
    return False

# Checks whether a string contains a weblink
def is_weblink(word):
    if re.match("([a-zA-Z]{1,})\.([a-zA-Z]{1,})", word) and word not in weblink_exceptions:
        return True
    return False

# Checks whether a string is an indicator of a live broadcast
def is_livebroadcast(word):
    return word in unfit_data_indicators

# Write data to txt file
def write_data(data, percentage, outfile):
    with open(outfile, 'w') as txtfile:
        txtfile.write(f"{percentage}% of data salvaged\n")
        [txtfile.write(path + '\n') for path in data]

if len(sys.argv) < 3:
    print("Please enter the data path and the outputfile")
else:
    # List of file paths that will be used for training
    filepaths, percentage = filter_vtt_data(sys.argv[1])
    write_data(filepaths, percentage, sys.argv[2])