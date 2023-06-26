from random import choice

POSSIBLE_PSW_LETTERS = [chr(c) for c in range(ord('A'), ord('Z') + 1)] + \
                       [chr(c) for c in range(ord('a'), ord('z') + 1)]


def main():
    psw_length = int(input())    # длина пароля
    psw = ''

    for _ in range(psw_length):
        psw_letter = choice(POSSIBLE_PSW_LETTERS)
        psw += psw_letter

    print(psw)


main()