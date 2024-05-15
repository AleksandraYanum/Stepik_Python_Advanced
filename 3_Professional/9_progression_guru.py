from sys import stdin


ARITHMETIC_PROGRESSION_MSG = 'Арифметическая прогрессия'
GEOMETRIC_PROGRESSION_MSG = 'Геометрическая прогрессия'
NOT_PROGRESSION_MSG = 'Не прогрессия'


def main():

    prev_num, curr_num = int(stdin.readline()), int(stdin.readline())

    difference = curr_num - prev_num
    quotient = curr_num / prev_num
    line_count = 0
    progression_count = 0
    
    for line in stdin:
        prev_num = curr_num
        curr_num = int(line)

        progression_count += 1 if curr_num - prev_num == difference else (-1 if curr_num / prev_num == quotient else 0)
        line_count += 1

    output = ARITHMETIC_PROGRESSION_MSG if progression_count == line_count else \
            (GEOMETRIC_PROGRESSION_MSG if progression_count == -line_count else NOT_PROGRESSION_MSG)
    
    print(output)


main()