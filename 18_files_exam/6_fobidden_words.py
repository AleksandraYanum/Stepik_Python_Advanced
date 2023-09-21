FORBIDDEN_WORD_CHAR = '*'


def find_all(source, symb):
    symbol_idx_list = []
    start_idx = 0
    symbol_idx = source.find(symb, start_idx)

    while symbol_idx != -1:
        symbol_idx_list.append(symbol_idx)
        start_idx = symbol_idx + 1
        symbol_idx = source.find(symb, start_idx)

    return symbol_idx_list


def main():
    new_line_list = []

    with open(input(), encoding='utf-8') as file, open('forbidden_words.txt',  encoding='utf-8') as words:

            forbidden_words = sorted(words.read().split(), key=len, reverse=True)
            forbidden_word_sizes = [len(word) for word in forbidden_words]

            for line in file:
                    lower_line = line.lower()
                    for word, size in zip(forbidden_words, forbidden_word_sizes):
                            word_start_idx_list = find_all(lower_line, word)
                            for start_idx in word_start_idx_list:
                                  line = line[:start_idx] + FORBIDDEN_WORD_CHAR * size + line[start_idx + size:]
                    new_line_list.append(line.strip())

    print(*new_line_list, sep='\n')


main()