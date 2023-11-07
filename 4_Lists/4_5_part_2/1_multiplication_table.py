ALIGNMENT_LENGTH = 3

# row_count, col_count = int(input()), int(input())
row_count, col_count = 6, 6

mult_table = []

for row in range(row_count):
    curr_row = []
    curr_elem = 0
    for col in range(col_count):
        curr_row.append(str(curr_elem).ljust(ALIGNMENT_LENGTH))
        curr_elem += row 
    mult_table.append(curr_row)

for row in mult_table:
    print(*row)