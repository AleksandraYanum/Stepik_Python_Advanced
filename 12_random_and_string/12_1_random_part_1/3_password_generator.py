from random import choice

FIRST_CHAR_KEY = 'first'
LAST_CHAR_KEY = 'last'

CHAR_RANGES = [{FIRST_CHAR_KEY: 'A', LAST_CHAR_KEY: 'Z'}, 
              {FIRST_CHAR_KEY: 'a', LAST_CHAR_KEY: 'z'}]

def main():
    psw_length = int(input())    # длина пароля
    psw = ''

    possible_psw_chars = []
    for char_range in CHAR_RANGES:
        chars = [chr(c) for c in range(ord(char_range[FIRST_CHAR_KEY]), ord(char_range[LAST_CHAR_KEY]) + 1)]
        possible_psw_chars.extend(chars)

    for _ in range(psw_length):
        psw_letter = choice(possible_psw_chars)
        psw += psw_letter

    print(psw)


main()