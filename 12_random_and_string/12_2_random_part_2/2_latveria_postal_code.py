from string import ascii_uppercase
from random import randint
from random import choice


LATVERIA_POSTAL_CODE_PATTERN = 'LetterLetterNumber_NumberLetterLetter'

UPPERCASE_LETTER_WORD = 'letter'    #uppercase letter
UPPERCASE_LETTER_CHAR = 'l'

NUM_WORD = 'number'   # from 0 to 99
NUM_CHAR = 'n'


FIRST_POS_NUM = 0
LAST_POS_NUM = 99


def generate_postal_code(postal_code_mask):
    postal_code = ''

    postal_code_mask_formatted = postal_code_mask.lower().\
        replace(UPPERCASE_LETTER_WORD, UPPERCASE_LETTER_CHAR).\
        replace(NUM_WORD, NUM_CHAR)

    print(postal_code_mask_formatted)

    for c in postal_code_mask_formatted:
        if c == UPPERCASE_LETTER_CHAR:
            postal_code_char = choice(ascii_uppercase)
        elif c == NUM_CHAR:
            postal_code_char = str(randint(FIRST_POS_NUM, LAST_POS_NUM))
        else:
            postal_code_char = c
        postal_code += postal_code_char
    
    return postal_code


def main():
    liveria_postal_code = generate_postal_code(LATVERIA_POSTAL_CODE_PATTERN)
    print(liveria_postal_code)


main()