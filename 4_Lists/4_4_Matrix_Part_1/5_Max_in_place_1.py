matrix_size = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(matrix_size)]
max_num = matrix[0][0]

for row in range(matrix_size):
    for col in range(row + 1):
        max_num = max(matrix[row][col], max_num)

print(max_num)
