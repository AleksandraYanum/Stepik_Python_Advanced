NO_ONE_LIKED = 'Никто не оценил данную запись'
ONE_PERSON_LIKED = '{name} оценил(а) данную запись'
TWO_PEOPLE_LIKED = '{first_name} и {second_name} оценили данную запись'
THREE_PEOPLE_LIKED = '{first_name}, {second_name} и {third_name} оценили данную запись'
A_LOT_OF_PEOPLE_LIKED = '{first_name}, {second_name} и {rest_amount_of_people} других оценили данную запись'


def likes(names):
    names_amount = len(names)
    if names_amount == 0:
        output_text = NO_ONE_LIKED
    elif names_amount == 1:
        output_text = ONE_PERSON_LIKED.format(name=names[0])
    elif names_amount == 2:
        output_text = TWO_PEOPLE_LIKED.format(first_name=names[0], second_name=names[1])       
    elif names_amount == 3:
        output_text = THREE_PEOPLE_LIKED.format(first_name=names[0], second_name=names[1], third_name=names[2])     
    else:
        output_text = A_LOT_OF_PEOPLE_LIKED.format(first_name=names[0], second_name=names[1], rest_amount_of_people=(names_amount - 2))
    
    return output_text


def main():
    print(likes([]))
    print(likes(['Тимур']))
    print(likes(['Тимур', 'Артур']))
    print(likes(['Тимур', 'Артур', 'Руслан']))
    print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
    print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
    print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))


main()