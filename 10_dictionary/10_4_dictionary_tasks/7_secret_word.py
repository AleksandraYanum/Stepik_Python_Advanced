def main():
    secret_word = input()
    secret_word_unique_chars = set(secret_word)

    # {AMOUNT: LETTER}
    letter_amount_dict = {}
    for _ in range(int(input())):
        letter, letter_amount = input().split(':')
        letter_amount_dict[int(letter_amount)] = letter
    
    # {SECRET_CHAR: AMOUNT}
    char_amount_dict = {}
    for char in secret_word_unique_chars:
        char_amount = secret_word.count(char)
        char_amount_dict[char] = char_amount

    decoded_word = secret_word
    for char in char_amount_dict:
        decoded_letter_amount = char_amount_dict[char]
        decoded_letter = letter_amount_dict[decoded_letter_amount]
        decoded_word = decoded_word.replace(char, decoded_letter)

    print(decoded_word)


main()