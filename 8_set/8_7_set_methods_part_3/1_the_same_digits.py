POSITIVE_OUTPUT = 'YES'
NEGATIVE_OUTPUT = 'NO'

set_1, set_2 = set(input()), set(input())

has_no_intersection = set_1.isdisjoint(set_2)

output = POSITIVE_OUTPUT
if has_no_intersection:
    output = NEGATIVE_OUTPUT

print(output)