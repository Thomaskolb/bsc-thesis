# Thomas Kolb s1027332
# This program filters data that is not useful for training the wav2vec2 model

import webvttparser
import sys
import os
import re

subtitle_ext = '.vtt'
weblink_exceptions = ['nos.nl', 'service.npo.nl']
live_broadcast_indicators = ['LIVEPROGRAMMA,', 'LIVEPROGRAMMA', 'LIVE', 'ONDERTITELD', 'ACHTERLOPEN']
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
            if meets_data_requirements(captions):
                filtered_paths.append(f"{folder}/{vttfile}")
        print("folder finished..")
    percentage = "{:.1f}".format((len(filtered_paths)/path_count)*100)
    return filtered_paths, percentage

# Function that decides whether data can be used
def meets_data_requirements(captions):
    for caption in [c.text.split() for c in captions]:
        for word in caption:
            if is_weblink(word) or is_livebroadcast(word) or len(captions) < 10:
                return False
    return True

# Checks whether a string contains a weblink
def is_weblink(word):
    if re.match("([a-zA-Z]{1,})\.([a-zA-Z]{1,})", word) and word not in weblink_exceptions:
        return True
    return False

# Checks whether a string is an indicator of a live broadcast
def is_livebroadcast(word):
    return word in live_broadcast_indicators

# Write data to txt file
def write_data(data, percentage):
    txtfile = open('filtered_data.txt', 'w')
    txtfile.write(f"{percentage}% of data salvaged\n")
    [txtfile.write(path + '\n') for path in data]
    txtfile.close()

if(len(sys.argv) < 2):
    print("Please enter the data path.")
else:
    # List of file paths that will be used for training
    filepaths, percentage = filter_vtt_data(sys.argv[1])
    write_data(filepaths, percentage)