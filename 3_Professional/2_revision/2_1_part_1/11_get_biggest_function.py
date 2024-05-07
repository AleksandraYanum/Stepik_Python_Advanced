def get_biggest(numbers):
    if numbers:
        
        num_strings = [str(i) for i in numbers]
        num_strings_length = len(num_strings)

        for i in range(num_strings_length):
            max_index = i

            for j in range(i + 1, num_strings_length):
                if num_strings[j] + num_strings[max_index] > num_strings[max_index] + num_strings[j]:
                    max_index = j

            num_strings[i], num_strings[max_index] = num_strings[max_index], num_strings[i]
            
        biggest_number = int(''.join(num_strings))
        
    else:
        biggest_number = -1
    
    return biggest_number



'''

Сравниваем пары соседних элементов и меняем их местами, чтобы бо́льший элемент стоял раньше.

Когда сравниваются две строки num_strings[j] и num_strings[max_index], чтобы определить, какая из них должна идти раньше в отсортированном списке, мы сравниваем результат конкатенации этих строк. Если конкатенация num_strings[j] + num_strings[max_index] даёт большее число, чем num_strings[index] + num_strings[j], то меняем местами строки num_strings[j] и num_strings[max_index].

После завершения сортировки строк в списке num_strings они будут расположены так, что конкатенация любых двух строк будет давать максимальное число.

max_index - использую для хранения индекса строки, которая должна идти первой при сравнении конкатенации строк внутри 

'''
