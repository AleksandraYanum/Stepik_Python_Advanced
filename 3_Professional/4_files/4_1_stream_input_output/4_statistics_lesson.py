import sys
from statistics import mean

EMPTY_INPUT_MSG = 'нет учеников'
TALLEST_HEIGHT_MSG = 'Рост самого высокого ученика: {}'
SHORTEST_HEIGHT_MSG = 'Рост самого низкого ученика: {}'
AVERAGE_HEIGHT_MSG = 'Средний рост: {}'


student_heights = []
185
for line in sys.stdin:
    current_height = int(line.strip())
    student_heights.append(current_height)

output = EMPTY_INPUT_MSG

if student_heights:

    min_height = min(student_heights)
    max_height = max(student_heights)
    average_height = mean(student_heights)

    output = '\n'.join([SHORTEST_HEIGHT_MSG.format(min_height), 
                    TALLEST_HEIGHT_MSG.format(max_height), 
                    AVERAGE_HEIGHT_MSG.format(average_height)])

print(output)
