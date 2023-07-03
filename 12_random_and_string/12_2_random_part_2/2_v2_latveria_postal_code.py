# Implemented version formates LATVERIA_POSTAL_CODE_PATTERN from 
# 'LetterLetterNumber_NumberLetterLetter' to 'lln_nll'. If postal code includes letters 'l', 'n'
# that should be ignored, it's needed to introduced new chars for encoding which don't occurs 
# in POSTAL_CODE_PATTERN


from string import ascii_uppercase
from random import randint
from random import choice


LATVERIA_POSTAL_CODE_PATTERN = 'LetterLetterNumber_NumberLetterLetter'

POSTAL_UPPERCASE_LETTER_WORD = 'letter'    #uppercase letter
POSTAL_UPPERCASE_LETTER_CHAR = 'l'

POSTAL_NUM_WORD = 'number'   # from 0 to 99
POSTAL_NUM_CHAR = 'n'

PATTERN_WORD_CHAR_DIC = {POSTAL_UPPERCASE_LETTER_WORD: POSTAL_UPPERCASE_LETTER_CHAR,
                         POSTAL_NUM_WORD: POSTAL_NUM_CHAR}

FIRST_POS_NUM = 0
LAST_POS_NUM = 99


def find_all(source, symb):
    symbol_idx_list = []
    start_idx = 0
    symbol_idx = source.find(symb, start_idx)

    while symbol_idx != -1:
        symbol_idx_list.append(symbol_idx)
        start_idx = symbol_idx + 1
        symbol_idx = source.find(symb, start_idx)

    return symbol_idx_list


# func takes not normalized postal code pattern, brings it into normalized form 
# (lowercase and single char coded) and calls enerate_postal_code_from_normalized_pattern func

def generate_postal_code(postal_code_mask, pattern_word_char_dic):
    
    postal_code_mask = postal_code_mask.lower()

    for pattern_word, pattern_char in pattern_word_char_dic.items():

        pattern_word_idx_list = find_all(postal_code_mask, pattern_word)

        first_idx = pattern_word_idx_list[0]
        last_idx = pattern_word_idx_list[len(pattern_word_idx_list) - 1]

        postal_code_mask_normalized = postal_code_mask[:first_idx]

        for i in range(len(pattern_word_idx_list) - 1):
            current_idx = pattern_word_idx_list[i]
            next_idx = pattern_word_idx_list[i + 1]

            postal_code_mask_normalized += pattern_char
            postal_code_mask_normalized += postal_code_mask[current_idx + len(pattern_word) : next_idx] 

        postal_code_mask_normalized += pattern_char + postal_code_mask[last_idx + len(pattern_word):]
        postal_code_mask = postal_code_mask_normalized
        
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


def main():
    
    latveria_postal_code = generate_postal_code(LATVERIA_POSTAL_CODE_PATTERN, PATTERN_WORD_CHAR_DIC)
    print(latveria_postal_code)


main()