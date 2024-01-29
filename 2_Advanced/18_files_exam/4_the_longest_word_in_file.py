with open('words.txt',  encoding='utf-8') as file:
        text = file.read().split()
        longest_words = [word for word in text if len(word) == len(max(text, key=len))]

print(*longest_words, sep='\n')