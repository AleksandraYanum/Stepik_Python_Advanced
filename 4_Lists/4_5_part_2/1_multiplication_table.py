ALIGNMENT_LENGTH = 3

# row_count, col_count = int(input()), int(input())
row_count, col_count = 5, 4

mult_table = []

# for row in range(row_count):
#     curr_row = []
#     curr_elem = 0
#     for col in range(col_count):
#         curr_row.append(str(curr_elem).ljust(ALIGNMENT_LENGTH))
#         curr_elem += row 
#     mult_table.append(curr_row)


# left_col - elems before main diag
# right_col - elems of main diag and after it

for row in range(min(row_count, col_count)):
    curr_row = []
    curr_elem = row
    for left_col in range(row):
        curr_row.append(mult_table[left_col][row])
    for right_col in range(row, col_count):
        curr_row.append(curr_elem)
        curr_elem += row
    mult_table.append(curr_row)

if col_count < row_count:
    for i in range(col_count, row_count):
        mult_table.append([(n * i) for n in range(col_count)])

for row in mult_table:
    print(*row)