from sys import stdin
from datetime import datetime


ASCENDING_MSG = 'ASC'
DESCENDING_MSG = 'DESC'
MIXED_MSG = 'MIX'
DATE_FROMAT = '%d.%m.%Y'

def main():

    prev_date = datetime.strptime(stdin.readline().strip(), DATE_FROMAT)
    order_count = 0
    date_count = 0

    for line in stdin:
        curr_date = datetime.strptime(line.strip(), DATE_FROMAT)
        order_count += 1 if prev_date < curr_date else (-1 if prev_date > curr_date else 0)
        date_count +=1
        prev_date = curr_date

    output = ASCENDING_MSG if order_count == date_count else (DESCENDING_MSG if order_count == -date_count else MIXED_MSG)

    print(output)


main()