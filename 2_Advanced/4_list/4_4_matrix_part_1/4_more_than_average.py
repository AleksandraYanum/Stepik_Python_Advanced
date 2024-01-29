arithmetic_mean = 0
result_arr = []

n = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(n)]

for row in range(n):
    num_count = 0
    arithmetic_mean = sum(matrix[row]) / n
    for col in range(n):
        if matrix[row][col] > arithmetic_mean:
            num_count += 1
    result_arr.append(num_count)

print(*result_arr, sep='\n')

# comment