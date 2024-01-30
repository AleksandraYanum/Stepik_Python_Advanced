POSITIVE_OUTPUT = 'YES'
NEGATIVE_OUTPUT = 'NO'


def is_anagram(string_1, string_2):
    result = False
    string_char_amount = {}

    for char in string_1:
        string_char_amount[char] = string_char_amount.get(char, 0) + 1
    for char in string_2:
        if char not in string_char_amount:
            break
        else:
            string_char_amount[char] = string_char_amount[char] - 1
            if string_char_amount[char] == 0:
                del string_char_amount[char]
    else:
        result = string_char_amount == {}

    return result


def main():
    string_1, string_2 = ''.join(c.lower() for c in input() if c.isalpha()), \
                         ''.join(c.lower() for c in input() if c.isalpha())

    anagram_found = is_anagram(string_1, string_2)

    output = POSITIVE_OUTPUT if anagram_found else NEGATIVE_OUTPUT
  
    print(output)

    
main()