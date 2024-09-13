from datetime import datetime, timedelta

DATE_PATTERN = '%d.%m.%Y'
DAY_AMOUNT = 10

start_date = datetime.strptime(input(), DATE_PATTERN)
curr_date = start_date

for i in range(1, DAY_AMOUNT + 1):
    print(curr_date.strftime(DATE_PATTERN))
    curr_date = curr_date + timedelta(days=i + 1)
