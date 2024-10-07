from csv import reader

DELIMITER_SYM = ','

col_num = int(input()) - 1

with open('deniro.csv', 'r', encoding='utf-8') as file:
    data = list(reader(file))

data.sort(key=lambda x: int(x[col_num]) if x[col_num].isdigit() else x[col_num])

for lst in data:
    print(*lst, sep=DELIMITER_SYM)
