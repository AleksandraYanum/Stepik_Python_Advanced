from string import ascii_lowercase
from string import ascii_uppercase
from string import digits
from random import sample


EXCEPTION_CHARS = set('lI1oO0')
PASSWORD_DIGITS = set(digits) - EXCEPTION_CHARS
PASSWORD_LOWERCASE = set(ascii_lowercase) - EXCEPTION_CHARS
PASSWORD_UPPERCASE = set(ascii_uppercase) - EXCEPTION_CHARS
ALL_PASSWORD_CHARS = ''.join(PASSWORD_DIGITS | PASSWORD_LOWERCASE |PASSWORD_UPPERCASE)


def generate_password_by_len(length, chars):
    password = ''.join(sample(chars, length))
    return password


def generate_passwords(amount, length, chars):
    password_list = [generate_password_by_len(length, chars) for _ in range(amount)]
    return password_list


def main():
    password_amount = int(input())
    password_len = int(input())
    passwords = generate_passwords(password_amount, password_len, ALL_PASSWORD_CHARS)

    print(*passwords, sep='\n')


main()
