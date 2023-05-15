MARKS = ' .,-_:!@#$%^&?'

def find_the_rarest_word(text, delimiters):
    word_list = text.lower().split()
    word_frequencies = {}
    for word in word_list:
        word = word.strip(delimiters)
        word_frequencies[word] = word_frequencies.get(word, 0) + 1
    
    min_frequency = min(word_frequencies.values())
    the_rarest_words = [word for word, amount in word_frequencies.items() if amount == min_frequency]
    the_rarest_word = min(the_rarest_words)
 
    return the_rarest_word


def main():
    input_text = input()
    the_rarest_word = find_the_rarest_word(input_text, MARKS)
    print(the_rarest_word)


main()
