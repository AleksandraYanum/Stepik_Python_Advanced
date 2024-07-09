from datetime import date


DAYS_PER_WEEK_AMOUNT = 7

weekday_count = [0] * DAYS_PER_WEEK_AMOUNT
END_YEAR = 9999
START_YEAR = 1
MONTH_AMOUNT = 12

NEEDED_DAY = 13


for year in range(START_YEAR, END_YEAR + 1):
    for month in range(1, MONTH_AMOUNT + 1):
        weekday_count[date(year, month, NEEDED_DAY).weekday()] += 1

print(*weekday_count, sep='\n')
