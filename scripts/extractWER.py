# Thomas Kolb s1027332
# This program generates a file containing the WER information of the output of 
# the trained wav2vec model and the actual labels of validation data
# It also does the same thing with asr data as hypothesis

import worderrorrate
import sys

# Name of output txt files
outname = 'word-checkpoint_best.pt-valid.txt'

# Line of equal chars
bar = '=' * 30

# Calculates WER for model data and captions and asr data and captions
def write_WER_data(evalpath, asrpath):
    with open(f'{evalpath}/WERdata_test.txt', 'w') as werfile:
        with open(f'{evalpath}/hypo.{outname}', 'r') as hypofile, \
                open(f'{evalpath}/ref.{outname}') as reffile, \
                open(f'{asrpath}/asr-test.txt', 'r') as asrfile, \
                open(f'{asrpath}/test.wrd', 'r') as asrreffile:
            avg_wer = 0
            avg_wer_asr = 0
            hypodata, refdata = hypofile.read().split('\n'), reffile.read().split('\n')
            asrlines, asrreflines = asrfile.read().split('\n'), asrreffile.read().split('\n')
            hypolines = [' '.join(dataline.split(' ')[:-1]) for dataline in hypodata]
            reflines = [' '.join(dataline.split(' ')[:-1]) for dataline in refdata]
            # Sort based on values of refdata
            hypolines = [x for _,x in sorted(zip(reflines, hypolines))]
            asrlines = [x for _,x in sorted(zip(asrreflines, asrlines))]
            reflines = sorted(reflines)
            asrreflines = sorted(asrreflines)
            for i in range(len(hypolines)):
                if len(reflines[i]) > 0:
                    werdata = worderrorrate.WER(reflines[i].split(' '), hypolines[i].split(' '))
                    asrwerdata = worderrorrate.WER(asrreflines[i].split(' '), asrlines[i].split(' '))
                    werfile.write(f'{werdata}WER = {werdata.wer()}\n')
                    werfile.write(f'{asrwerdata}ASR_WER = {asrwerdata.wer()}\n{bar}\n\n')
                    avg_wer += werdata.wer()
                    avg_wer_asr += asrwerdata.wer()
            werfile.write(f'average wer = {avg_wer/len(hypolines)}\n')
            werfile.write(f'average wer asr = {avg_wer_asr/len(asrlines)}\n')

if len(sys.argv) < 3:
    print("Please enter the path with refs & hypos and the path for the asr lines")
else:
    write_WER_data(sys.argv[1], sys.argv[2])


# TODO verschil wer met asr data

