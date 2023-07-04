# Implemented version irnores letters 'l', 'n' and encodes only words 'letter', 'number'


from string import ascii_uppercase
from random import randint
from random import choice


LATVERIA_POSTAL_CODE_PATTERN = 'ABCLetterDEFLetterNumber_NumberLetterLetterAA'

POSTAL_UPPERCASE_LETTER_WORD = 'letter'    #uppercase letter
POSTAL_NUM_WORD = 'number'   # from 0 to 99

POSTAL_UPPERCASE_LETTER_CHAR = 'l'
POSTAL_NUM_CHAR = 'n'

PATTERN_WORD_LIST = [POSTAL_UPPERCASE_LETTER_WORD, POSTAL_NUM_WORD]

FIRST_POS_NUM = 0
LAST_POS_NUM = 99

##############################################################################

# Version 1

# func takes not normalized postal code pattern, brings it into normalized form 
# (lowercase and single char coded) and calls enerate_postal_code_from_normalized_pattern func
def generate_postal_code(postal_code_mask):

    postal_code_mask_normalized = postal_code_mask.lower().\
        replace(POSTAL_UPPERCASE_LETTER_WORD, POSTAL_UPPERCASE_LETTER_CHAR).\
        replace(POSTAL_NUM_WORD, POSTAL_NUM_CHAR)

    postal_code = generate_postal_code_from_normalized_pattern(postal_code_mask_normalized)

    return postal_code


def generate_postal_code_from_normalized_pattern(postal_code_mask_normalized):

    postal_code = ''
    for c in postal_code_mask_normalized:
        if c == POSTAL_UPPERCASE_LETTER_CHAR:
            postal_code_char = choice(ascii_uppercase)
        elif c == POSTAL_NUM_CHAR:
            postal_code_char = str(randint(FIRST_POS_NUM, LAST_POS_NUM))
        else:
            postal_code_char = c
        postal_code += postal_code_char

    return postal_code

##############################################################################

# Version 2

def find_all(source, symb):
    symbol_idx_list = []
    start_idx = 0
    symbol_idx = source.find(symb, start_idx)

    while symbol_idx != -1:
        symbol_idx_list.append(symbol_idx)
        start_idx = symbol_idx + 1
        symbol_idx = source.find(symb, start_idx)

    return symbol_idx_list


def generate_postal_code_v2(pattern, pattern_word_list):
    
    pattern = pattern.lower()

    for pattern_word in pattern_word_list:
        pattern_word_len = len(pattern_word)
        pattern_word_idx_list = find_all(pattern, pattern_word)

        first_idx = pattern_word_idx_list[0]
        last_idx = pattern_word_idx_list[-1]
        postal_code = pattern[:first_idx]

        for i in range(len(pattern_word_idx_list) - 1):
            current_idx = pattern_word_idx_list[i]
            next_idx = pattern_word_idx_list[i + 1]

            postal_code_value = generate_postal_code_value(pattern_word)
            postal_code += postal_code_value
            postal_code += pattern[current_idx + pattern_word_len:next_idx] 

        postal_code += generate_postal_code_value(pattern_word) + \
                                    pattern[last_idx + pattern_word_len:]

        pattern = postal_code
        
    return postal_code


def generate_postal_code_value(pattern_word):
    
    value = ''
    if pattern_word == POSTAL_UPPERCASE_LETTER_WORD:
        value = choice(ascii_uppercase)
    elif pattern_word == POSTAL_NUM_WORD:
        value = str(randint(FIRST_POS_NUM, LAST_POS_NUM))
    
    return value

##############################################################################

# Version 3

def generate_postal_code_v3(pattern, pattern_word_list):
    postal_code = pattern.lower()

    for pattern_word in pattern_word_list:
        pattern_word_idx_list = find_all(postal_code, pattern_word)
        first_idx = pattern_word_idx_list[0]
        last_idx = pattern_word_idx_list[-1]
        postfix_start_idx = last_idx + len(pattern_word)
        pattern_to_code = postal_code[first_idx:postfix_start_idx]
        pattern_prefix = postal_code[:first_idx]
        pattern_postfix = postal_code[postfix_start_idx:]
        pattern_word_amount = pattern_to_code.count(pattern_word)

        for _ in range(pattern_word_amount):
            postal_code_value = generate_postal_code_value(pattern_word)
            pattern_to_code = pattern_to_code.\
                              replace(pattern_word, postal_code_value, 1)

        postal_code = pattern_prefix + pattern_to_code + pattern_postfix

    return postal_code

##############################################################################

# Version 4

def generate_postal_code_v4(pattern, pattern_word_list):
    postal_code = ''
    start_pattern_word_end_dic = {}
    postal_code_low = pattern.lower()

    for pattern_word in pattern_word_list:
        pattern_word_len = len(pattern_word)
        pattern_word_idx_list = find_all(postal_code_low, pattern_word)
        for word_idx in pattern_word_idx_list:
            start_idx = word_idx
            start_pattern_word_end_dic[start_idx] = {pattern_word: start_idx + pattern_word_len - 1}
            # POSSIBLE TO ADD TYPES?

    start_pattern_word_end_dic_sorted = dict(sorted(start_pattern_word_end_dic.items()))

    prev_end_idx = -1
    for start_idx, word_end in start_pattern_word_end_dic_sorted.items():
        for word, end_idx in word_end.items():   

            postal_code_value = generate_postal_code_value(word)
            postal_code += postal_code_low[prev_end_idx + 1:start_idx] 
            postal_code += postal_code_value 
            prev_end_idx = end_idx

    postal_code += postal_code_low[prev_end_idx + 1:]

    return postal_code
            
##############################################################################


def main():
    
    latveria_postal_code = generate_postal_code_v4(LATVERIA_POSTAL_CODE_PATTERN, PATTERN_WORD_LIST)
    print(latveria_postal_code)


main()