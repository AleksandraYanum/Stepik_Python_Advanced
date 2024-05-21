from sys import stdin
from operator import truediv, sub


ARITHMETIC_PROGRESSION = sub
GEOMETRIC_PROGRESSION = truediv
NOT_PROGRESSION = 3

PROGRESSION_OUTPUT = {
    ARITHMETIC_PROGRESSION: 'Арифметическая прогрессия',
    GEOMETRIC_PROGRESSION: 'Геометрическая прогрессия',
    NOT_PROGRESSION:  'Не прогрессия'
}
                      

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
    step = None

    if curr_num - prev_num == prev_num - prev_prev_num:
        progression_type = ARITHMETIC_PROGRESSION
        step = curr_num - prev_num
    elif curr_num / prev_num == prev_num / prev_prev_num:
        progression_type = GEOMETRIC_PROGRESSION
        step = curr_num / prev_num

    if progression_type != NOT_PROGRESSION: 
            
        if not is_right_progression_in_stdin(progression_type, curr_num, step):
            progression_type = NOT_PROGRESSION
          
    output = PROGRESSION_OUTPUT[progression_type]
    
    print(output)


main()