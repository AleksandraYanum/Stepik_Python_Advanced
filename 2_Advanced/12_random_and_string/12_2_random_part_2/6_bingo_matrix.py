from random import sample

ROW_COUNT = 5
COL_COUNT = 5

FIRST_POSSIBLE_NUM = 1
LAST_POSSIBLE_NUM = 75
CENTER_NUM = 0


def main():
    num_amount = ROW_COUNT * COL_COUNT
    bingo_nums = sample(range(FIRST_POSSIBLE_NUM, LAST_POSSIBLE_NUM), num_amount)
    bingo_matrix = [bingo_nums[i:i+COL_COUNT] for i in range(0, len(bingo_nums), COL_COUNT)]
    bingo_matrix[ROW_COUNT // 2][COL_COUNT // 2] = CENTER_NUM

    for row in range(ROW_COUNT):
        for col in range(COL_COUNT):
            print(str(bingo_matrix[row][col]).ljust(3), end='')
        print()


main()