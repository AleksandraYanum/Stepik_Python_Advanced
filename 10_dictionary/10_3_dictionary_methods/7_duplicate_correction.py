def fix_duplicates(text):
    word_list = text.split()
    deduplicated_word_list = []
    word_duplicate_amount = {}
    for word in word_list:
        if word not in  deduplicated_word_list:
            deduplicated_word_list.append(word)
        else:
            word_duplicate_amount[word] = word_duplicate_amount.get(word, 0) + 1
            deduplicated_word_list.append(word + '_' + str(word_duplicate_amount[word]))

    deduplicated_text = ' '.join(deduplicated_word_list)

    return deduplicated_text


def main():
    input_text = input()
    deduplicated_text = fix_duplicates(input_text)

    print(deduplicated_text)


main()
