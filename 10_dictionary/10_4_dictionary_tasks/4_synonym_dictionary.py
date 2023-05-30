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


# def find_synonym(synonyms, input_word):
#     input_word_synonym = synonyms.get(input_word)

#     if input_word_synonym == None:
#         key_list = list(synonyms.keys())
#         value_list = list(synonyms.values())
#         input_word_synonym = key_list[value_list.index(input_word)]

#     return input_word_synonym


# def main():

#     synonyms = {}
#     for _ in range(int(input())):
#         word, synonym = input().split()
#         synonyms[word] = synonym

#     input_word = input()

#     input_word_synonym = find_synonym(synonyms, input_word)

#     print(input_word_synonym)


# main()