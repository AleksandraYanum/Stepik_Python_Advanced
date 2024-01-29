CURRENCY_CHAR = '$'


total_price = 0

with open('ledger.txt',  encoding='utf-8') as file:
    for line in file:
        total_price += int(line.rstrip('\n').lstrip(CURRENCY_CHAR))

print(f'{CURRENCY_CHAR}{total_price}')