def main():
    secret_word = input()

    # {AMOUNT: LETTER}
    letter_amount_dict = {}
    for _ in range(int(input())):
        letter, letter_amount = input().split(':')
        letter_amount_dict[int(letter_amount)] = letter
    
    # {SECRET_CHAR: AMOUNT}
    char_amount_dict = {}
    for char in secret_word:
        char_amount_dict[char] = char_amount_dict.get(char, 0) + 1

    decoded_word = secret_word
    for char in char_amount_dict:
        decoded_letter_amount = char_amount_dict[char]
        decoded_letter = letter_amount_dict[decoded_letter_amount]
        decoded_word = decoded_word.replace(char, decoded_letter)

    print(decoded_word)


main()