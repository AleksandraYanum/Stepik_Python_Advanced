def main():
    matrix_size = int(input())

    matrix = [[int(num) for num in input().split()] for _ in range(matrix_size)]

    max_matrix_num = matrix[0][0]
    for row in range(matrix_size // 2 + matrix_size % 2):
        for col in range(row + 1):
            current_max_num = max([matrix[row][col],
                                   matrix[row][matrix_size - col - 1],
                                   matrix[matrix_size - row - 1][matrix_size - col - 1],
                                   matrix[matrix_size - row - 1][col]
                                   ])
            max_matrix_num = max(max_matrix_num, current_max_num)

    print(max_matrix_num)


main()
# My super comment
