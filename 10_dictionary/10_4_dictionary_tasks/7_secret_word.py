def main():
    secret_word = input()
    secret_word_set = set(secret_word)

    letters_amount = {}
    for _ in range(int(input())):
        letter, amount = input().split(':')
        letters_amount[amount] = letter
    
    print(secret_word_set)
    print(letters_amount)    

    secret_chars_amount = {}
    for char in secret_word_set:
        char_amount = secret_word.count(char)
        secret_chars_amount[char] = char_amount

    print(secret_chars_amount)


main()