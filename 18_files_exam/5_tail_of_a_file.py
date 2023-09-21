LINE_AMOUNT = 10

file_tail = []

with open(input(),  encoding='utf-8') as file:
        for line in file:
                if len(file_tail) == LINE_AMOUNT:
                        file_tail.pop(0)
                file_tail.append(line.strip())

                
print(*file_tail, sep='\n')