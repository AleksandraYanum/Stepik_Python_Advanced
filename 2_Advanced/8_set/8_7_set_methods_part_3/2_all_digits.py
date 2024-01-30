POSITIVE_OUTPUT = 'YES'
NEGATIVE_OUTPUT = 'NO'

set_1, set_2 = set(input()), set(input())

is_sub_set = set_2.issubset(set_1)

if is_sub_set:
    output = POSITIVE_OUTPUT
else:
    output = NEGATIVE_OUTPUT

print(output)
