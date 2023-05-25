POSITIVE_OUTPUT = 'YES'
NEGATIVE_OUTPUT = 'NO'


def main():
    
    word_1, word_2 = sorted(input()), sorted(input())
    is_anagram = word_1 == word_2

    if is_anagram:
        output = POSITIVE_OUTPUT
    else:
        output = NEGATIVE_OUTPUT

    print(output)


main()