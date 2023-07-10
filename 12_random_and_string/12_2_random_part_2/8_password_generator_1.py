from string import ascii_letters
from string import digits
from random import sample


EXCEPTION_CHARS = 'lI1oO0'
PASSWORD_CHARS = ''.join(set(ascii_letters) | set(digits) - set(EXCEPTION_CHARS))


def generate_password_by_len(length, chars):
    password = ''.join(sample(chars, length))
    return password


def generate_passwords(amount, length, chars):
    password_list = [generate_password_by_len(length, PASSWORD_CHARS) for _ in range(amount)]
    return password_list


def main():
    password_amount = int(input())
    password_len = int(input())
    passwords = generate_passwords(password_amount, password_len, PASSWORD_CHARS)

    print(*passwords, sep='\n')


main()
