solder_list = list(range(1, int(input()) + 1))
step = int(input())

while len(solder_list) > 1:
    for _ in range(step - 1):
        solder_list.append(solder_list[0])
        solder_list.pop(0)
    solder_list.pop(0)


remaining_solder = solder_list[0]


print(remaining_solder)