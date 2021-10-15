# Thomas Kolb s1027332
# This program contains functions to parse a caption text to match the appropriate rules for training

from num2words import num2words
from nltk.tokenize import word_tokenize
import re

import nltk
nltk.download('punkt')

interpunction = ['.', '...', '!', '?']
forbidden_formats = ['.{1,}\-.{1,}', '[A-Z]{1,}\:', '[0-9]{1,}\.[0-9]{1,}', '[0-9]{1,}e']

# Function that filters out captions that don't match requirements
# If it is acceptable it will return an edited caption text
def acceptable_caption_text(caption_text):
    word_list = word_tokenize(caption_text)
    new_word_list = []
    follow_with_capital = False
    for word in word_list:
        # Filter for all upper letters, star symbol and regex formats
        if (word.isupper() and len(word) > 1) or word == '*' or any([re.match(exp, word) for exp in forbidden_formats]):
            return ''
        word = number_to_words(word)
        # Capitalize word after interpunction (except ',')
        if follow_with_capital:
            word = word.capitalize()
            follow_with_capital = False
        new_word_list.append(word)
        if word in interpunction:
            follow_with_capital = True
    # Capitalize first word
    new_word_list[0] = new_word_list[0].capitalize()
    return ' '.join(new_word_list)

# Function that tries to parse string to a number, if that goes turn it into a word
def number_to_words(word):
    try:
        num = int(word)
        word = num2words(num, lang='nl')
    except:
        pass
    return word
