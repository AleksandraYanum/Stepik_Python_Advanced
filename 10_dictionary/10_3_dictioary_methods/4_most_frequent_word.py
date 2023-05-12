text_words = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange ' \
    'barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot ' \
    'currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon ' \
    'pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple ' \
    'barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit ' \
    'banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate ' \
    'barley'.split()

word_amounts = {}
for word in text_words:
    word_amounts[word] = word_amounts.get(word, 0) + 1

max_amount = max(word_amounts.values())
most_frequent_words = [word for word, amount in word_amounts.items() if amount == max_amount]

most_frequent_word = min(most_frequent_words)

print(most_frequent_word)