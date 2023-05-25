def main():
    programmer_data =  [(input().split(':')) for i in range(int(input()))]
    programmer_dict = {i[0].lower(): i[1].strip() for i in programmer_data}

    # also it's possible to split print and logic: append values to list 
    for word in [input().lower() for i in range(int(input()))]:
        print(programmer_dict.get(word, "Не найдено"))


main()