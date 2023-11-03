from collections import deque 

solders = deque(range(1, int(input()) + 1))
step = int(input())

while len(solders) > 1:
    for _ in range(step - 1):
        solders.append(solders[0])
        solders.popleft()
    solders.popleft()


remaining_solder = solders[0]


print(remaining_solder) 