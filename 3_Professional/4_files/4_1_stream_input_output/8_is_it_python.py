from sys import stdin
from datetime import datetime


ASC_ORDER = 1
DESC_ORDER = 2
MIX_ORDER = 3

ASC_MSG = 'ASC'
DESC_MSG = 'DESC'
MIX_MSG = 'MIX'
DATE_FROMAT = '%d.%m.%Y'


def is_asc_order(prev_value, curr_value):
    result = curr_value > prev_value
    return result


def is_desc_order(prev_value, curr_value):
    result = curr_value < prev_value
    return result


def main():

    prev_date = datetime.strptime(stdin.readline().strip(), DATE_FROMAT)
    curr_date = datetime.strptime(stdin.readline().strip(), DATE_FROMAT)

    date_order = ASC_ORDER if curr_date > prev_date else (DESC_ORDER if curr_date < prev_date else MIX_ORDER)
    compare_func = is_asc_order if date_order == ASC_ORDER else is_desc_order

    prev_date = curr_date

    if date_order != MIX_ORDER:

        for line in stdin:
            curr_date = datetime.strptime(line.strip(), DATE_FROMAT)

            if not compare_func(prev_date, curr_date):
                date_order = MIX_ORDER
                break
            
            prev_date = curr_date

    output = ASC_MSG if date_order == ASC_ORDER else (DESC_MSG if date_order == DESC_ORDER else MIX_MSG)

    print(output)


main()