from collections import defaultdict


def def_value():
    empty_set = set()
    return empty_set


def main():
    country_table = [input().split() for _ in range(int(input()))]
    city_country_dict = defaultdict(def_value)

    for country_row in country_table:
        for city in country_row[1:]:
            city_country_dict[city].add(country_row[0])

    country_output_list = []

    for _ in range(int(input())):
        input_city = input()
        country_output_list.append(city_country_dict[input_city])

    for country in country_output_list:
        print(*country)


main()