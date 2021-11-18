# Thomas Kolb s1027332
# This program reads all the collected results from training and finds the captions that performed better than the ASR

import sys

# Active configuration
active_config = 2

# File name to analyse
wer_data_file = 'WERdata_test.txt'

# Line of equal chars
bar = '=' * 30

# Function that finds the well performed captions with list of paths and writes them to output file
def write_data(outfile, paths):
    for path in paths:
        with open(outfile, 'w') as outfile, open(f'{path}/{wer_data_file}', 'r') as infile:
            lines = infile.read().split('\n')
            refs = lines[0:-3:10]
            hyps = lines[1:-3:10]
            asrs = lines[5:-3:10]
            asr_values = lines[7:-3:10]
            values = lines[3:-3:10]
            for i in range(len(values)):
                value = values[i].split(' ')[-1]
                asr_value = asr_values[i].split(' ')[-1]
                if value > asr_value:
                    outfile.write(f'{value} > {asr_value}\n{refs[i]}\n{hyps[i]}\n{asrs[i]}\n{bar}\n\n')

if len(sys.argv) < 2:
    print("Please enter the output file and the configuration data paths")
else:
    write_data(sys.argv[1], sys.argv[2:])