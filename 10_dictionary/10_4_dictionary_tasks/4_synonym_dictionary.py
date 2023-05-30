def main():

    synonyms = {}
    for _ in range(int(input())):
        word, synonym = input().split()
        synonyms[word] = synonym
        synonyms[synonym] = word

    input_word = input()

    input_word_synonym = synonyms[input_word]
    print(input_word_synonym)


main()