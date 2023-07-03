# Implemented version irnores letters 'l', 'n' and encodes only words 'letter', 'number'


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


def generate_postal_code(pattern, pattern_word_char_dic):
    
    pattern = pattern.lower()

    for pattern_word, pattern_char in pattern_word_char_dic.items():

        pattern_word_idx_list = find_all(pattern, pattern_word)
        first_idx = pattern_word_idx_list[0]
        last_idx = pattern_word_idx_list[len(pattern_word_idx_list) - 1]
        postal_code = pattern[:first_idx]

        for i in range(len(pattern_word_idx_list) - 1):
            current_idx = pattern_word_idx_list[i]
            next_idx = pattern_word_idx_list[i + 1]

            postal_code_value = generate_postal_code_value(pattern_char)
            postal_code += postal_code_value
            postal_code += pattern[current_idx + len(pattern_word) : next_idx] 

        postal_code += generate_postal_code_value(pattern_char) + \
                                    pattern[last_idx + len(pattern_word):]

        pattern = postal_code
        
    return postal_code


def generate_postal_code_value(pattern_char):
    
    value = ''
    if pattern_char == POSTAL_UPPERCASE_LETTER_CHAR:
        value = choice(ascii_uppercase)
    elif pattern_char == POSTAL_NUM_CHAR:
        value = str(randint(FIRST_POS_NUM, LAST_POS_NUM))
    
    return value


def main():
    
    latveria_postal_code = generate_postal_code(LATVERIA_POSTAL_CODE_PATTERN, PATTERN_WORD_CHAR_DIC)
    print(latveria_postal_code)


main()