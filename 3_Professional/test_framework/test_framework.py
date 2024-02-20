# Implement test func:
# 1. Read input file with test data from Stepik
# 2. Merge #1 with file to test and save to new file
# 3. Execute #2 file and save output to result file
# 4. Compare #3 with the expected output file and write comparison results

FILE_PATH = 'C:\\Users\\Aleksandra\\src\\Stepik_Python_Advanced\\3_Professional\\test_framework\\'


def test():
    with open(FILE_PATH + 'code.py', encoding='utf-8') as code_file, \
     open(FILE_PATH + 'to_be_tested.py', 'w', encoding='utf-8') as to_be_tested_file:
        for line in code_file:
            to_be_tested_file.write(line)

    with open(FILE_PATH + 'input.txt', encoding='utf-8') as input_file, \
     open(FILE_PATH + 'to_be_tested.py', 'w', encoding='utf-8') as to_be_tested_file:
        for line in input_file:
            to_be_tested_file.write(line)        

test()