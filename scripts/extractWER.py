# Thomas Kolb s1027332
# This program generates a file containing the WER information of the output of 
# the trained wav2vec model and the actual labels of validation data

import worderrorrate
import sys

# Name of output txt files
outname = 'word-checkpoint_best.pt-valid.txt'

# Line of equal chars
bar = ['='] * 30

def write_WER_data(path):
    with open(f'{path}/WERdata.txt', 'w') as werfile:
        with open(f'{path}/hypo.{outname}', 'r') as hypofile, open(f'{path}/ref.{outname}') as reffile:
            avg_wer = 0
            hypodata, refdata = hypofile.read().split('\n'), reffile.read().split('\n')
            hypolines = [' '.join(dataline.split(' ')[:-1]) for dataline in hypodata]
            reflines = [' '.join(dataline.split(' ')[:-1]) for dataline in refdata]
            for i in range(len(hypodata)):
                if len(reflines[i]) > 0:
                    werdata = worderrorrate.WER(reflines[i].split(' '), hypolines[i].split(' '))
                    werfile.write(f'{werdata}\nWER = {werdata.wer()}\n{bar}\n')
                    avg_wer += werdata.wer()
            werfile.write(f'average wer = {avg_wer/len(hypolines)}')

if len(sys.argv) < 2:
    print("Please enter the data path")
else:
    write_WER_data(sys.argv[1])

