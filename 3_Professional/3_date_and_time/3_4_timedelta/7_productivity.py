#Using one-liner

from datetime import datetime, timedelta

DATE_PATTERN = '%d.%m.%Y'
DAY_AMOUNT = 10

start_date = datetime.strptime(input(), DATE_PATTERN)

print("\n".join([(start_date + timedelta(days=sum(range(2, i+2)))).strftime(DATE_PATTERN) for i in range(DAY_AMOUNT)]))