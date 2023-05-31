def main():
    input_lists = [input().split() for _ in range(int(input()))]

    city_country_dict = {}
    for input_list in input_lists:
        for city in input_list[1:]:
            city_country_dict[city] = input_list[0]

    country_output_list = []
    for _ in range(int(input())):
        input_city = input()
        country_output_list.append(city_country_dict[input_city])
        
    for country in country_output_list:
        print(country)


main()