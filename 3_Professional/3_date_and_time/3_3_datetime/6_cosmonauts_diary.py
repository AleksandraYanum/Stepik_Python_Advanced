from datetime import datetime


DATETIME_FORMAT = '%d.%m.%Y; %H:%M'
DATETIME_IDX = 0
DIARY_TEXT_IDX = 1

diary_entries = {}  # Use a dictionary instead of a list

with open('diary.txt', 'r', encoding='utf-8') as file:
    entry_lines = []
    for line in file:
        line = line.strip()
        if line:
            entry_lines.append(line)
        else:
            date_time = datetime.strptime(entry_lines[0], DATETIME_FORMAT)
            text = '\n'.join(entry_lines[1:])
            diary_entries[date_time] = text  # Store entry in the dictionary
            entry_lines = []

    if entry_lines:
        date_time = datetime.strptime(entry_lines[0], DATETIME_FORMAT)
        text = '\n'.join(entry_lines[1:])
        diary_entries[date_time] = text  # Store entry in the dictionary

sorted_entries = sorted(diary_entries.items(), key=lambda x: x[0])

for entry in sorted_entries:
    print(entry[0].strftime(DATETIME_FORMAT))
    print(entry[1])
    print()
