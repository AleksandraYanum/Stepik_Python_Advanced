import csv
from collections import defaultdict


DISTRICT_POS = 1
HOTSPOT_POS = 3


district_hotspot_dict = defaultdict(int)

with open('wifi.csv', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)  # skip title

    for row in reader:
        district = row[DISTRICT_POS]
        hotspot_amount = int(row[HOTSPOT_POS])
        district_hotspot_dict[district] += hotspot_amount

# sort by hotspot amount and alphabet
sorted_districts = sorted(district_hotspot_dict.items(), key=lambda x: (-x[1], x[0]))

for district, hotspot_amount in sorted_districts:
    print(f'{district}: {hotspot_amount}')