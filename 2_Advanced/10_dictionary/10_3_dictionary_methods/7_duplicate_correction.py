PATTERN_WORD_CHAR = 'w'
PATTERN_NUM_CHAR = 'n'
DEFAULT_PATTERN = 'w_n'


def fix_duplicates(text, pattern=DEFAULT_PATTERN):
    word_list = text.split()
    deduplicated_word_list = []
    word_duplicate_amount = {}
    for word in word_list:
        if word not in  deduplicated_word_list:
            deduplicated_word_list.append(word)
        else:
            word_duplicate_amount[word] = word_duplicate_amount.get(word, 0) + 1
            deduplicated_word = pattern.replace(PATTERN_WORD_CHAR, word).\
                                        replace(PATTERN_NUM_CHAR, str(word_duplicate_amount[word]))
            deduplicated_word_list.append(deduplicated_word)

    deduplicated_text = ' '.join(deduplicated_word_list)

    return deduplicated_text


###################################################################################

DUPLICATE_PATTERN = 'w(n)'


def main():
    input_text = input()
    # deduplicated_text = fix_duplicates(input_text, DUPLICATE_PATTERN)
    deduplicated_text = fix_duplicates(input_text)

    print(deduplicated_text)


main()
