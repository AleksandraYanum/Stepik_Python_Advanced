NAME_NOT_FOUND = ['абонент не найден']


def main():
    phone_book = {}

    for _ in range(int(input())):
        found_phone_num, name = input().split()
        phone_set = set()
        phone_book.setdefault(name.lower(), phone_set).add(found_phone_num)

    found_phone_num_list = []
    for _ in range(int(input())):
        input_name = input().lower()
        found_phone_num_list.append(phone_book.get(input_name, NAME_NOT_FOUND))

    for found_phone_num in found_phone_num_list:
        print(*found_phone_num)


main()