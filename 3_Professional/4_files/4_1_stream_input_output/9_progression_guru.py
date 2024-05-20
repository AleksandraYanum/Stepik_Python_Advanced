from sys import stdin


ARITHMETIC_PROGRESSION = 1
GEOMETRIC_PROGRESSION = 2
NOT_PROGRESSION = 3

ARITHMETIC_PROGRESSION_MSG = 'Арифметическая прогрессия'
GEOMETRIC_PROGRESSION_MSG = 'Геометрическая прогрессия'
NOT_PROGRESSION_MSG = 'Не прогрессия'


def main():

    prev_prev_num, prev_num, curr_num = int(stdin.readline()), int(stdin.readline()), int(stdin.readline())

    progression = NOT_PROGRESSION
    difference, quotient = None, None

    if curr_num - prev_num == prev_num - prev_prev_num:
        progression = ARITHMETIC_PROGRESSION
        difference = curr_num - prev_num
    elif curr_num / prev_num == prev_num / prev_prev_num:
        progression = GEOMETRIC_PROGRESSION
        quotient = curr_num / prev_num

    if progression != NOT_PROGRESSION: 
            
            for line in stdin:
                prev_num = curr_num
                curr_num = int(line)

                if  (curr_num - prev_num != difference and progression == ARITHMETIC_PROGRESSION) or \
                    (curr_num / prev_num != quotient and progression == GEOMETRIC_PROGRESSION):
                     progression = NOT_PROGRESSION
                     break

    output = ARITHMETIC_PROGRESSION_MSG if progression == ARITHMETIC_PROGRESSION else \
            (GEOMETRIC_PROGRESSION_MSG if progression == GEOMETRIC_PROGRESSION else NOT_PROGRESSION_MSG)
    
    print(output)


main()