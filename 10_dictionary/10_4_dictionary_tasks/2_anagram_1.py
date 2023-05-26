POSITIVE_OUTPUT = 'YES'
NEGATIVE_OUTPUT = 'NO'


def main():
    word_letter_amount = {}

    for letter in input().lower():
        word_letter_amount[letter] = word_letter_amount.get(letter, 0) + 1
    for letter in input().lower():
        word_letter_amount[letter] = word_letter_amount.get(letter, 0) - 1

    is_anagram = set(word_letter_amount.values()) == {0}
    output = POSITIVE_OUTPUT if is_anagram else NEGATIVE_OUTPUT
  
    print(output)


main()