# Thomas Kolb s1027332
# This program takes a file and extracts all the unique characters, including their occurence

import sys

# Function that extracts the unique characters and their occurence in a dict
def extract_alphabet(path):
    char_dict = {}
    with open(path, 'r') as ltrfile:
        for char in [c for c in ltrfile.read() if c != ' ']:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 0
    return dict(sorted(char_dict.items(), key=lambda x: x[1]))

# Function that writes data to output file
def write_dict_file(data, outpath):
    with open(outpath, 'w') as outfile:
        [outfile.write(f'{char}\t{data[char]}\n') for char in data]
    

if len(sys.argv) < 3:
    print("Please enter the path of the ltr file and the output file")
else:
    write_dict_file(extract_alphabet(sys.argv[1]), sys.argv[2])