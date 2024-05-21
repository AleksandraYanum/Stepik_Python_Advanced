from sys import stdin
from operator import truediv, sub


ARITHMETIC_PROGRESSION = sub
GEOMETRIC_PROGRESSION = truediv
NOT_PROGRESSION = 3

ARITHMETIC_PROGRESSION_MSG = 'Арифметическая прогрессия'
GEOMETRIC_PROGRESSION_MSG = 'Геометрическая прогрессия'
NOT_PROGRESSION_MSG = 'Не прогрессия'


def is_right_progression_in_stdin(progression_type, curr_num, step):

    for line in stdin:
        prev_num = curr_num
        curr_num = int(line)
        result = progression_type(curr_num, prev_num) == step

        if not result:
            break

    return result
    

def main():

    prev_prev_num, prev_num, curr_num = int(stdin.readline()), int(stdin.readline()), int(stdin.readline())

    progression_type = NOT_PROGRESSION
    difference, quotient = None, None

    if curr_num - prev_num == prev_num - prev_prev_num:
        progression_type = ARITHMETIC_PROGRESSION
        difference = curr_num - prev_num
    elif curr_num / prev_num == prev_num / prev_prev_num:
        progression_type = GEOMETRIC_PROGRESSION
        quotient = curr_num / prev_num

    if progression_type != NOT_PROGRESSION: 
            
            if progression_type == ARITHMETIC_PROGRESSION:
                if not is_right_progression_in_stdin(ARITHMETIC_PROGRESSION, curr_num, difference):
                    progression_type = NOT_PROGRESSION

            if progression_type == GEOMETRIC_PROGRESSION:
                if not is_right_progression_in_stdin(GEOMETRIC_PROGRESSION, curr_num, quotient):
                    progression_type = NOT_PROGRESSION
          
    output = ARITHMETIC_PROGRESSION_MSG if progression_type == ARITHMETIC_PROGRESSION else \
            (GEOMETRIC_PROGRESSION_MSG if progression_type == GEOMETRIC_PROGRESSION else NOT_PROGRESSION_MSG)
    
    print(output)


main()