import sys

EMPTY_INPUT_MSG = 'нет учеников'
TALLEST_HEIGHT_MSG = 'Рост самого высокого ученика: {}'
SHORTEST_HEIGHT_MSG = 'Рост самого низкого ученика: {}'
AVERAGE_HEIGHT_MSG = 'Средний рост: {}'


min_height, max_height = 1000, -1
total_height_sum = 0
student_count = 0

for line in sys.stdin:
    current_height = int(line)

    if current_height < min_height:
        min_height = current_height
    if current_height > max_height:
        max_height = current_height

    total_height_sum += current_height
    student_count += 1

output = EMPTY_INPUT_MSG

if student_count:

    average_height = total_height_sum / student_count

    output = '\n'.join([SHORTEST_HEIGHT_MSG.format(min_height), 
                    TALLEST_HEIGHT_MSG.format(max_height), 
                    AVERAGE_HEIGHT_MSG.format(average_height)])

print(output)
