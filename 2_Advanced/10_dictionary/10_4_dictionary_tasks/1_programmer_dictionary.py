def main():
    programmer_slang_dict = {i[0].lower(): i[1].strip() for i in \
        [input().split(':') for j in range(int(input()))]}

    # also it's possible to split print and logic: append values to list 
    for word in [input().lower() for i in range(int(input()))]:
        print(programmer_slang_dict.get(word, "Не найдено"))


main()