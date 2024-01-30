UPPER_QUARTER_TEXT = "Верхняя четверть"
LOWER_QUARTER_TEXT = "Нижняя четверть"
LEFT_QUARTER_TEXT = "Левая четверть"
RIGHT_QUARTER_TEXT = "Правая четверть"


def get_upper_quarter_sum(matrix, size):
    total = 0
    start = 1
    stop = size - 1

    for row in range(size // 2):
        for col in range(start, stop):
            total += matrix[row][col]
        start += 1
        stop -= 1

    return total


def get_lower_quarter_sum(matrix, size):
    total = 0
    stop = size // 2 + 1
    start = size - stop

    for row in range(size // 2 + 1, size):
        for col in range(start, stop):
            total += matrix[row][col]
        start -= 1
        stop += 1

    return total


def get_left_quarter_sum(matrix, size):
    total = 0

    for row in range(1, size // 2 + size % 2):
        for col in range(row):
            total += matrix[row][col]

    stop = size // 2 - 1

    for row in range(size // 2 + size % 2, size - 1):
        for col in range(stop):
            total += matrix[row][col]
        stop -= 1

    return total


def get_right_quarter_sum(matrix, size):
    total = 0

    for row in range(1, size // 2 + size % 2):
        for col in range(size - row, size):
            total += matrix[row][col]
        start = row + 2

    for row in range(size // 2 + size % 2, size - 1):
        for col in range(start, size):
            total += matrix[row][col]
        start += 1

    return total


def get_quarter_sums(matrix, size):
    upper_sum = get_upper_quarter_sum(matrix, size)
    right_sum = get_right_quarter_sum(matrix, size)
    lower_sum = get_lower_quarter_sum(matrix, size)
    left_sum = get_left_quarter_sum(matrix, size)
    
    return upper_sum, right_sum, lower_sum, left_sum


def main():
    matrix_size = int(input())
    matrix = [[int(num) for num in input().split()] for _ in range(matrix_size)]

    upper_quarter_sum, right_quarter_sum, lower_quarter_sum, left_quarter_sum = get_quarter_sums(matrix, matrix_size)

    print(f'{UPPER_QUARTER_TEXT}: {upper_quarter_sum}')
    print(f'{RIGHT_QUARTER_TEXT}: {right_quarter_sum}')
    print(f'{LOWER_QUARTER_TEXT}: {lower_quarter_sum}')
    print(f'{LEFT_QUARTER_TEXT}: {left_quarter_sum}')


main()




