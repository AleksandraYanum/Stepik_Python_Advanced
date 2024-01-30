# LINE_AMOUNT = 10

# file_tail = []

# with open(input(),  encoding='utf-8') as file:
#         for line in file:
#                 if len(file_tail) == LINE_AMOUNT:
#                         file_tail.pop(0)
#                 file_tail.append(line.strip())

                
# print(*file_tail, sep='\n')

#***************************************************************************************************************

# Deque is preferred over a list in the cases where we need quicker append or pop operations from 
# both the ends of the container. This is possible because Python's deque is implemented as a doubly linked list. 

from collections import deque as de


REQUIRED_LINE_AMOUNT = 10

file_tail = de([])
line_amount = 0

with open(r'C:\Users\Aleksandra\Downloads\text.txt',  encoding='utf-8') as file:
        for line in file:
                file_tail.append(line.strip())
                line_amount += 1
                if line_amount > REQUIRED_LINE_AMOUNT:
                        file_tail.popleft()

print(*file_tail, sep='\n')
