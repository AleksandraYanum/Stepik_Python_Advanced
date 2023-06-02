def main():
    secret_word = input()

    # {AMOUNT: LETTER}
    letter_amount_dict = {}
    for _ in range(int(input())):
        letter, letter_amount = input().split(':')
        letter_amount_dict[int(letter_amount)] = letter
    
    # {SECRET_CHAR: [AMOUNT]}
    char_amount_dict = {}
    for char in secret_word:
        result_list = char_amount_dict.get(char, [0])
        result_list[0] += 1
        char_amount_dict[char] = result_list
  
    # Third combined dict {SECRET_CHAR: [AMOUNT, LETTER]}
    for char in char_amount_dict:
        need_amount = char_amount_dict[char][0]
        need_letter = letter_amount_dict[need_amount]
        char_amount_dict[char].append(need_letter)

    decoded_word = ''
    for char in secret_word:
        decoded_letter = char_amount_dict[char][1]
        decoded_word += decoded_letter

    print(decoded_word)


main()