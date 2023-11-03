from collections import deque 

soldiers = deque(range(1, int(input()) + 1))
step = int(input())
soldier_amount = len(soldiers)

while soldier_amount > 1:
    for _ in range(step - 1):
        soldiers.append(soldiers[0])
        soldiers.popleft()
    soldiers.popleft()
    soldier_amount -= 1

remaining_soldier = soldiers[0]

print(remaining_soldier) 