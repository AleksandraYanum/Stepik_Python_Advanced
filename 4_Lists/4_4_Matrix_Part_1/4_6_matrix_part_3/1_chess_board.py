EVEN_SYM = '.'
ODD_SYM = '+'

EVEN_CHAR_CODE = 0
ODD_CHAR_CODE = 1


def print_visual_matrix(matrix, row_count, col_count):
    for row in range(row_count):
        for col in range(col_count):
            if matrix[row][col] == ODD_CHAR_CODE:
                print(ODD_SYM, end=' ')
            else:
                print(EVEN_SYM, end=' ')
        print()


def set_matrix_staggered_old(matrix, row_count, col_count):
    for row in range(row_count):
        for col in range(1, col_count, 2):
            matrix[row][col] = ODD_CHAR_CODE


def set_matrix_staggered(matrix, row_count, col_count):

    for row in range(row_count):
        for col in range((row + 1) % 2, col_count, 2):
            matrix[row][col] = ODD_CHAR_CODE


def main():
    row_count, col_count = [int(i) for i in input().split()]
    matrix = [[EVEN_CHAR_CODE] * col_count for _ in range(row_count)]

    set_matrix_staggered(matrix, row_count, col_count)

    print_visual_matrix(matrix, row_count, col_count)


main()
