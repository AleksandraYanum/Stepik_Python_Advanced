from string import ascii_uppercase
from random import randint
from random import choice


LIVERIA_POSTAL_CODE_PATTERN = 'LetterLetterNumber_NumberLetterLetter'

UPPERCASE_LETTER_CODE = 'letter'    #uppercase letter
NUM_CODE = 'number'   # from 0 to 99

FIRST_POS_NUM = 0
LAST_POS_NUM = 99

def generate_postal_code(postal_code_mask):
    postal_code = ''

    for c in postal_code_mask:
        if c == UPPERCASE_LETTER_CODE:
            postal_code_char = choice(ascii_uppercase)
        elif c == NUM_CODE:
            postal_code_char = str(randint(FIRST_POS_NUM, LAST_POS_NUM))
        else:
            postal_code_char = c
        postal_code += postal_code_char
    
    return postal_code

    


def main():
    liveria_postal_code = generate_postal_code(LIVERIA_POSTAL_CODE_PATTERN)
    print(liveria_postal_code)


main()