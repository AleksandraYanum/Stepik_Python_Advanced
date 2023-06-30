from string import ascii_uppercase
from random import randint
from random import choice

# Implemented version formates LATVERIA_POSTAL_CODE_PATTERN from 
# 'LetterLetterNumber_NumberLetterLetter' to 'lln_nll'. If postal code includes letters 'l', 'n'
# that should be ignored, it's needed to introduced new chars for encoding which don't occurs 
# in POSTAL_CODE_PATTERN


LATVERIA_POSTAL_CODE_PATTERN = 'LetterLetterNumber_NumberLetterLetter'

POSTAL_UPPERCASE_LETTER_WORD = 'letter'    #uppercase letter
POSTAL_UPPERCASE_LETTER_CHAR = 'l'

POSTAL_NUM_WORD = 'number'   # from 0 to 99
POSTAL_NUM_CHAR = 'n'

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
def generate_postal_code(postal_code_mask):
    
    postal_code_mask_low = postal_code_mask.lower()

    postal_uppercase_letter_idx_list = find_all(postal_code_mask_low, POSTAL_UPPERCASE_LETTER_WORD)
    postal_number_idx_list = find_all(postal_code_mask_low, POSTAL_NUM_WORD)


    first_idx = postal_uppercase_letter_idx_list[0]
    last_idx = postal_uppercase_letter_idx_list[len(postal_uppercase_letter_idx_list) - 1]

    postal_code_mask_normalized = postal_code_mask_low[:first_idx]

    for i in range(len(postal_uppercase_letter_idx_list) - 1):
        current_idx = postal_uppercase_letter_idx_list[i]
        next_idx = postal_uppercase_letter_idx_list[i + 1]

        postal_code_mask_normalized += POSTAL_UPPERCASE_LETTER_CHAR
        postal_code_mask_normalized += postal_code_mask_low[current_idx + len(POSTAL_UPPERCASE_LETTER_WORD) : next_idx] 

    postal_code_mask_normalized += POSTAL_UPPERCASE_LETTER_CHAR + postal_code_mask_low[last_idx + len(POSTAL_UPPERCASE_LETTER_WORD):]
    
    print(postal_code_mask_normalized)

        
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
    latveria_postal_code = generate_postal_code(LATVERIA_POSTAL_CODE_PATTERN)
    print(latveria_postal_code)


main()