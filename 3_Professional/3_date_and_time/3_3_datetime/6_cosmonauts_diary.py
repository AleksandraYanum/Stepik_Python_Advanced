from datetime import datetime
from collections import defaultdict


DATETIME_FORMAT = '%d.%m.%Y; %H:%M'
DATETIME_IDX = 0
DIARY_TEXT_IDX = 1

diary_entries = defaultdict(list)  # Use a dictionary instead of a list

with open('C:\\Users\\Aleksandra\\Downloads\\diary.txt', 'r', encoding='utf-8') as file:
    is_first_line = True

    for line in file:
        line = line.strip()
        if line:
            if is_first_line:
                date_time = datetime.strptime(line, DATETIME_FORMAT)
                is_first_line = False
            else:
                diary_entries[date_time].append(line)  # Store entry in the dictionary
        else:
            is_first_line = True

sorted_entries = sorted(diary_entries.items(), key=lambda x: x[0])

for date, entries in sorted_entries:
    print(date.strftime(DATETIME_FORMAT))
    print(*entries, sep='\n')
    print()
