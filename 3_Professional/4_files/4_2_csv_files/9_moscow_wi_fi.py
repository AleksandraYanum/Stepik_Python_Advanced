from csv import DictReader
from collections import defaultdict


DELIMITER_CSV = ';'
DISTRICT_CSV = 'district'
ACCESS_POINTS_CSV = 'number_of_access_points'


district_access_point_dict = defaultdict(int)

with open('wifi.csv', encoding='utf-8') as file:
    wifi_data = DictReader(file, delimiter=DELIMITER_CSV)

    for row in wifi_data:
        district = row[DISTRICT_CSV]
        access_point_amount = int(row[ACCESS_POINTS_CSV])
        district_access_point_dict[district] += access_point_amount

# sort by hotspot amount and alphabet
sorted_districts = sorted(district_access_point_dict.items(), key=lambda x: (-x[1], x[0]))

for district, access_point_amount in sorted_districts:
    print(f'{district}: {access_point_amount}')