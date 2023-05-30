def find_synonym(synonyms, input_word):
    input_word_synonym = ''
    
    for word, synonym in synonyms.items():
        if input_word == word:
            input_word_synonym = synonym
            break
        elif input_word == synonym:
            input_word_synonym = word
            break
    
    return input_word_synonym


def main():
    synonyms = dict([[word for word in input().split()] for i in range(int(input()))])
    input_word = input()

    synonym = find_synonym(synonyms, input_word)
    
    print(synonym)



main()