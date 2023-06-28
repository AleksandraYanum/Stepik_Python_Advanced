purchased_goods = {}

for _ in range(int(input())):
    name, good, amount = input().split()
    purchased_goods[name][good] = purchased_goods.setdefault(name, {}).setdefault(good, 0) + int(amount)

for name in sorted(purchased_goods):
    print(f'{name}:')
    for purchase in sorted(purchased_goods[name].items()):
        print(*purchase)
