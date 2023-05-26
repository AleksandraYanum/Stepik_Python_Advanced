POSITIVE_OUTPUT = 'YES'
NEGATIVE_OUTPUT = 'NO'


def main():
    is_anagram = False
    word_letter_amount = {}

    for letter in input().lower():
        word_letter_amount[letter] = word_letter_amount.get(letter, 0) + 1
    for letter in input().lower():
        word_letter_amount[letter] = word_letter_amount.get(letter, 0) - 1
        if word_letter_amount[letter] < 0:
            break
    else:
        is_anagram = set(word_letter_amount.values()) == {0}

    output = POSITIVE_OUTPUT if is_anagram else NEGATIVE_OUTPUT
  
    print(output)


main()