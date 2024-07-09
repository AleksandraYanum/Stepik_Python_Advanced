from sys import stdin


EMPTY_INPUT_MSG = 'нет учеников'
TALLEST_HEIGHT_MSG = 'Рост самого высокого ученика: {}'
SHORTEST_HEIGHT_MSG = 'Рост самого низкого ученика: {}'
AVERAGE_HEIGHT_MSG = 'Средний рост: {}'


def main():
    line = stdin.readline().strip()

    if line:

        curr_height = int(line)
        min_height, max_height = curr_height, curr_height
        total_height_sum = curr_height
        student_count = 1

        for line in stdin:
            current_height = int(line)

            if current_height > max_height:
                max_height = current_height
            elif current_height < min_height:
                min_height = current_height
            
            total_height_sum += current_height
            student_count += 1
        
        average_height = total_height_sum / student_count

        output = '\n'.join([SHORTEST_HEIGHT_MSG.format(min_height), 
                            TALLEST_HEIGHT_MSG.format(max_height), 
                            AVERAGE_HEIGHT_MSG.format(average_height)])
    
    else:

        output = EMPTY_INPUT_MSG
      
    print(output)


main()
