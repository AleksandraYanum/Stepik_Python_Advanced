def main():
    secret_word = input()

    letter_amount = {}
    for _ in range(int(input())):
        letter, amount = input().split(':')
        letter_amount[amount] = letter

    print(letter_amount)


main()