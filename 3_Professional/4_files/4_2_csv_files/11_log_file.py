from csv import DictReader, DictWriter
from datetime import datetime


DELIMITER_SYM = ','
USERNAME_TITLE = 'username'
EMAIL_TITLE = 'email'
DATETIME_TITLE = 'dtime'
DATETIME_PATTERN = '%d/%m/%Y %H:%M'


logs = {}

with open('name_log.csv', 'r', encoding='utf-8') as file_read:
    rows = DictReader(file_read, delimiter=DELIMITER_SYM)
    
    for row in rows:
        email = row[EMAIL_TITLE]
        current_time = datetime.strptime(row[DATETIME_TITLE], DATETIME_PATTERN)

        if email in logs:
            existing_time = datetime.strptime(logs[email][DATETIME_TITLE], DATETIME_PATTERN)
            if current_time > existing_time:
                logs[email] = row
        else:
            logs[email] = row

with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as file_write:
    writer = DictWriter(file_write, fieldnames=[USERNAME_TITLE, EMAIL_TITLE, DATETIME_TITLE])
    writer.writeheader()
    
    for log in sorted(logs.values(), key=lambda x: x[EMAIL_TITLE]):
        writer.writerow(log)
