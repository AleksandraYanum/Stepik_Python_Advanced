STRING_DELIMITER = '-' * 10
TOTAL_SIZE_STRING = 'Summary: {size} {unit}'
UNIT_CONVERTION_DICT = {'B': 1, 'KB': 1024, 'MB': 1024 ** 2, 'GB': 1024 ** 3}
UNIT_DICT = {0: 'В', 1: 'КВ', 2: 'MB', 3: 'GB'}


def convert_to_biggest_unit(size):
    base = 1024
    for unit in UNIT_CONVERTION_DICT:
        if size > base:
            size /= base
        else:
            break
    
    return round(size), unit
    
    
def main():
    
    file_info = dict()
    
    with open('C:\\Users\\Aleksandra\\Downloads\\files.txt', encoding='utf-8') as file:

        for line in file:
            full_name, size, unit = line.split()
            name, extension = full_name.split('.')
            file_info.setdefault(extension, []).append((name, int(size) * UNIT_CONVERTION_DICT[unit]))

    for extension in sorted(file_info):
        total_size = 0
        for name, size in sorted(file_info[extension]):
            print(name + '.' + extension)
            total_size += size
            
        converted_size, converted_unit = convert_to_biggest_unit(total_size)
        print(STRING_DELIMITER)
        print(TOTAL_SIZE_STRING.format(size=converted_size, unit=converted_unit))
        print()
        

main()