# Thomas Kolb s1027332
# This program creates an LM using all the caption files

import webvttparser
import captionparser
import sys
import os

# Extension of subtitle files
subtitle_ext = '.vtt'

# Function that traverses all 'webm.vtt' files within a given directory
# and outputs an ltr file containing all lines separated by |
def generateLMfile(path, outfile):
    with open(f'{outfile}', 'w') as linesfile:
        for folder in os.listdir(path):
            vttfiles = [f for f in os.listdir(f"{path}/{folder}") if os.path.splitext(f)[1] == subtitle_ext]
            for vttfile in vttfiles:
                captions = webvttparser.read(f"{path}/{folder}/{vttfile}")
                for caption in captions:
                    new_caption_text = captionparser.acceptable_caption_text(caption.text, '|')
                    if len(new_caption_text) > 0:
                        linesfile.write(f'{new_caption_text}\n')

if len(sys.argv) < 3:
    print("Please enter the data path and the output file")
else:
    generateLMfile(sys.argv[1], sys.argv[2])