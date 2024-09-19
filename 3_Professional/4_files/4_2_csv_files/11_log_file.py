from csv import DictReader, DictWriter
from datetime import datetime
from collections import defaultdict


DELIMITER_SYM = ','
USERNAME_COL_NAME = 'username'
EMAIL_COL_NAME = 'email'
DATETIME_COL_NAME = 'dtime'
DATETIME_PATTERN = '%d/%m/%Y %H:%M'


latest_name_changes = defaultdict(lambda: None)


with open('name_log.csv', 'r', encoding='utf-8') as file_read:
    name_changes = DictReader(file_read, delimiter=DELIMITER_SYM)
    
    for name_change in name_changes:
        email = name_change[EMAIL_COL_NAME]
        change_time = datetime.strptime(name_change[DATETIME_COL_NAME], DATETIME_PATTERN)

        # if no record yet or if new change_time is later than the stored one
        if latest_name_changes[email] is None or change_time > datetime.strptime(latest_name_changes[email][DATETIME_COL_NAME], DATETIME_PATTERN):
            latest_name_changes[email] = name_change


with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as file_write:
    writer = DictWriter(file_write, fieldnames=[USERNAME_COL_NAME, EMAIL_COL_NAME, DATETIME_COL_NAME])
    writer.writeheader()
    
    for log in sorted(latest_name_changes.values(), key=lambda x: x[EMAIL_COL_NAME]):
        writer.writerow(log)
