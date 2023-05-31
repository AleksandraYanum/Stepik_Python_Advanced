def main():
    phone_book = {}

    for i in range(int(input())):
        phone_num, name = input().split()
        phone_book.setdefault(name.lower(), []).append(phone_num)

    print(phone_book)



main()