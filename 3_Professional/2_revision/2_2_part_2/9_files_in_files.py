from collections import defaultdict

FILE_INFO = defaultdict(lambda: defaultdict(list))
TOTAL_SIZE_CODE = 'total_size'
NAMES_CODE = 'names'
SIZES_CODE = 'sizes'
UNIT_CODE = 'unit'
FILE_INFO_VALUE_CODES = [NAMES_CODE, SIZES_CODE]
UNIT_CONVERTION_DICT = {'B': 1, 'KB': 1024, 'MB': 1024 ** 2, 'GB': 1024 ** 3}
FILE_PATH = 'C:\\Users\\Aleksandra\\Downloads\\'
FILE_NAME = 'files.txt'
STRING_DELIMITER = '-' * 10
TOTAL_SIZE_STRING = 'Summary: {size} {unit}'



def convert_to_biggest_unit(size):
    base = 1024
    for unit in UNIT_CONVERTION_DICT:
        if size > base:
            size /= base
        else:
            break
    
    return round(size), unit
    
    
def main():
    
    with open(FILE_PATH + FILE_NAME, encoding='utf-8') as file:

        for line in file:
            full_name, size, unit = line.split()
            name, extension = full_name.split('.')
            byte_size =  int(size) * UNIT_CONVERTION_DICT[unit]
            for code, value in zip(FILE_INFO_VALUE_CODES, [name, byte_size]):
                FILE_INFO[extension][code].append(value)

    for extension in FILE_INFO:
        total_size = sum(FILE_INFO[extension][SIZES_CODE])
        byte_size, converted_unit = convert_to_biggest_unit(total_size)

        FILE_INFO[extension][TOTAL_SIZE_CODE].append(byte_size)
        FILE_INFO[extension][UNIT_CODE].append(converted_unit)

    for extension in sorted(FILE_INFO):
        for name in sorted(FILE_INFO[extension][NAMES_CODE]):
            print(name + '.' + extension)
        print(STRING_DELIMITER)
        print(TOTAL_SIZE_STRING.format(size=FILE_INFO[extension][TOTAL_SIZE_CODE][0], 
                                        unit=FILE_INFO[extension][UNIT_CODE][0]))
        print()


main()