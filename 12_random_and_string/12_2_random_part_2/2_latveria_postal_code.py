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


def generate_postal_code(postal_code_mask):
    postal_code = ''

    postal_code_mask_formatted = postal_code_mask.lower().\
        replace(POSTAL_UPPERCASE_LETTER_WORD, POSTAL_UPPERCASE_LETTER_CHAR).\
        replace(POSTAL_NUM_WORD, POSTAL_NUM_CHAR)

    print(postal_code_mask_formatted)

    for c in postal_code_mask_formatted:
        if c == POSTAL_UPPERCASE_LETTER_CHAR:
            postal_code_char = choice(ascii_uppercase)
        elif c == POSTAL_NUM_CHAR:
            postal_code_char = str(randint(FIRST_POS_NUM, LAST_POS_NUM))
        else:
            postal_code_char = c
        postal_code += postal_code_char
    
    return postal_code


def main():
    liveria_postal_code = generate_postal_code(LATVERIA_POSTAL_CODE_PATTERN)
    print(liveria_postal_code)


main()