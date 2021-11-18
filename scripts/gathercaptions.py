# Thomas Kolb s1027332
# This program reads all the collected results from training and finds the captions that performed better than the ASR

import sys

# Active configuration
active_config = 2

# File name to analyse
wer_data_file = 'WERdata_test.txt'

# Line of equal chars
bar = '=' * 30

# type of test currently being analyzed
value_test = False
interpunction_test = True

# List of interpunction symbols - no '.' because it is not interesting
interpunction = [',', '!', '?', '-', ':']

# Function that finds the well performed captions with list of paths and writes them to output file
def write_data(outpath, paths):
    for path in paths:
        with open(outpath, 'w') as outfile, open(f'{path}/{wer_data_file}', 'r') as infile:
            lines = infile.read().split('\n')
            refs = lines[0:-3:10]
            hyps = lines[1:-3:10]
            asrs = lines[5:-3:10]
            asr_values = lines[7:-3:10]
            values = lines[3:-3:10]
            for i in range(len(values)):
                value = values[i].split(' ')[-1]
                asr_value = asr_values[i].split(' ')[-1]
                if ((not value_test or value < asr_value) 
                        and (not interpunction_test or any([word in interpunction for word in hyps[i][5:].split(' ')]))):
                    outfile.write(f'val {value} - asr {asr_value}\nREF={refs[i][5:]}\nHYP={hyps[i][5:]}\nASR={asrs[i][5:]}\n{bar}\n\n')

if len(sys.argv) < 2:
    print("Please enter the output file and the configuration data paths")
else:
    write_data(sys.argv[1], sys.argv[2:])