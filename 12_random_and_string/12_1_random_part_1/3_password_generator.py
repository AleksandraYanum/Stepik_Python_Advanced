from random import randint

FIRST_UPPERCASE_LETTER_CODE = ord('A')
LAST_UPPERCASE_LETTER_CODE = ord('Z')

FIRST_LOWERCASE_LETTER_CODE = ord('a')
LAST_LOWERCASE_LETTER_CODE = ord('z')

UPPERCASE_CODE = 1
LOWERCASE_CODE = 2

def main():
    
    psw_length = int(input())    # длина пароля
    psw = ''

    for _ in range(psw_length):
        letter_case_choise = randint(UPPERCASE_CODE, LOWERCASE_CODE)
        if letter_case_choise == UPPERCASE_CODE:
            psw_letter = chr(randint(FIRST_UPPERCASE_LETTER_CODE, LAST_UPPERCASE_LETTER_CODE))
        else:
            psw_letter = chr(randint(FIRST_LOWERCASE_LETTER_CODE, LAST_LOWERCASE_LETTER_CODE))
        psw += psw_letter

    print(psw)


main()