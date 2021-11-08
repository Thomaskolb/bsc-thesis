# Thomas Kolb s1027332
# This program takes a file and extracts all the unique words

import sys

# Function that extracts the unique words in a list
def extract_words(path):
    word_list = []
    print("START")
    with open(path, 'r') as ltrfile:
        for lines in ltrfile.read().split('\n'):
            print("LINE")
            print(lines)
            for word in lines.split('|'):
                print('WORD')
                print(word)
                if word not in word_list:
                    word_list.append(word)
    return dict(sorted(word_list))

# Function that writes data to output file
def write_lexicon_file(word_list, outpath):
    with open(outpath, 'w') as outfile:
        [outfile.write(f'{" ".join(list(word))}\n') for word in word_list]
    
if len(sys.argv) < 3:
    print("Please enter the path of the ltr file and the output file")
else:
    write_lexicon_file(extract_words(sys.argv[1]), sys.argv[2])