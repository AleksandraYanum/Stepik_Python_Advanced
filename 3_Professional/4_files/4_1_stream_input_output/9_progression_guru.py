from sys import stdin
from operator import truediv, sub


ARITHMETIC_PROGRESSION_FUNC = sub
GEOMETRIC_PROGRESSION_FUNC = truediv
NOT_PROGRESSION_FUNC = None

PROGRESSION_OUTPUT = {
    ARITHMETIC_PROGRESSION_FUNC: 'Арифметическая прогрессия',
    GEOMETRIC_PROGRESSION_FUNC: 'Геометрическая прогрессия',
    NOT_PROGRESSION_FUNC:  'Не прогрессия'
}
                      

def is_right_progression_in_stdin(progression_func, init_num, step):

    curr_num = init_num
    result = False

    for line in stdin:
        prev_num = curr_num
        curr_num = int(line)
        result = progression_func(curr_num, prev_num) == step

        if not result:
            break

    return result
    

def main():

    prev_prev_num, prev_num, curr_num = int(stdin.readline()), int(stdin.readline()), int(stdin.readline())

    progression_func = NOT_PROGRESSION_FUNC
    step = None

    if curr_num - prev_num == prev_num - prev_prev_num:
        progression_func = ARITHMETIC_PROGRESSION_FUNC
        step = curr_num - prev_num
    elif curr_num / prev_num == prev_num / prev_prev_num:
        progression_func = GEOMETRIC_PROGRESSION_FUNC
        step = curr_num / prev_num

    if progression_func != NOT_PROGRESSION_FUNC:
            
        if not is_right_progression_in_stdin(progression_func, curr_num, step):
            progression_func = NOT_PROGRESSION_FUNC
          
    output = PROGRESSION_OUTPUT[progression_func]
    
    print(output)


main()