from collections import deque 

solders = deque(range(1, int(input()) + 1))
step = int(input())
solder_amount = len(solders)

while solder_amount > 1:
    for _ in range(step - 1):
        solders.append(solders[0])
        solders.popleft()
    solders.popleft()
    solder_amount -= 1

remaining_solder = solders[0]

print(remaining_solder) 