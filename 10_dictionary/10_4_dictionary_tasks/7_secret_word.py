def main():
    secret_word = input()
    secret_word_unique_chars = set(secret_word)

    # {AMOUNT: LETTER}
    letter_amount_dict = {}
    for _ in range(int(input())):
        letter, letter_amount = input().split(':')
        letter_amount_dict[int(letter_amount)] = letter
    
    # {SECRET_CHAR: AMOUNT}
    secret_chars_amount_dict = {}
    for secret_char in secret_word_unique_chars:
        secret_char_amount = secret_word.count(secret_char)
        secret_chars_amount_dict[secret_char] = secret_char_amount

    decoded_word = secret_word
    for secret_char in secret_chars_amount_dict:
        decoded_letter_amount = secret_chars_amount_dict[secret_char]
        decoded_letter = letter_amount_dict[decoded_letter_amount]
        decoded_word = decoded_word.replace(secret_char, decoded_letter)

    print(decoded_word)


main()