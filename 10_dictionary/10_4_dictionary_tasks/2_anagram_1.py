POSITIVE_OUTPUT = 'YES'
NEGATIVE_OUTPUT = 'NO'


def main():
    is_anagram = False
    word_letter_amount = {}

    for letter in input().lower():
        word_letter_amount[letter] = word_letter_amount.get(letter, 0) + 1
    for letter in input().lower():
        if letter not in word_letter_amount.keys():
            break
        else:
            word_letter_amount[letter] = word_letter_amount.get(letter) - 1
            if word_letter_amount[letter] < 0:
                break
            if word_letter_amount[letter] == 0:
                del word_letter_amount[letter]
    else:
        is_anagram = word_letter_amount == {}

    output = POSITIVE_OUTPUT if is_anagram else NEGATIVE_OUTPUT
  
    print(output)


main()