# If not for Stepik, it is necessary to check that the password is not less than 
# the minimum password length

from string import ascii_lowercase
from string import ascii_uppercase
from string import digits
from random import sample
from random import shuffle


EXCEPTION_CHARS = set('lI1oO0')
PASSWORD_DIGITS = set(digits) - EXCEPTION_CHARS
PASSWORD_LOWERCASE = set(ascii_lowercase) - EXCEPTION_CHARS
PASSWORD_UPPERCASE = set(ascii_uppercase) - EXCEPTION_CHARS
MIN_PASSWORD_LENGTH = 3


def generate_password_by_len(length, digits, lowercase, uppercase):
    all_chars = ''.join(digits | lowercase | uppercase)
    password = sample(digits, 1) + sample(lowercase, 1) + sample(uppercase, 1) + \
                       sample(all_chars, length - MIN_PASSWORD_LENGTH)
    shuffle(password)
    password = ''.join(password)

    return password


def generate_passwords(amount, length, digits, lowercase, uppercase):
    password_list = [generate_password_by_len(length, digits, lowercase, uppercase) \
                     for _ in range(amount)]
    return password_list


def main():
    password_amount = int(input())
    password_len = int(input())
    passwords = generate_passwords(password_amount, password_len, PASSWORD_DIGITS, \
                                   PASSWORD_LOWERCASE, PASSWORD_UPPERCASE)

    print(*passwords, sep='\n')


main()
