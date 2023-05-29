POSITIVE_OUTPUT = 'YES'
NEGATIVE_OUTPUT = 'NO'


def is_anagram(string_1, string_2):
    result = False
    word_letter_amount = {}

    for letter in string_1:
        word_letter_amount[letter] = word_letter_amount.get(letter, 0) + 1
    for letter in string_2:
        if letter not in word_letter_amount:
            break
        else:
            word_letter_amount[letter] = word_letter_amount[letter] - 1
            if word_letter_amount[letter] == 0:
                del word_letter_amount[letter]
    else:
        result = word_letter_amount == {}

    return result


def main():
    string_1, string_2 = ''.join(c.lower() for c in input() if c.isalpha()), \
                         ''.join(c.lower() for c in input() if c.isalpha())

    output = POSITIVE_OUTPUT if is_anagram(string_1, string_2) else NEGATIVE_OUTPUT
  
    print(output)

    





main()