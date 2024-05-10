from datetime import datetime


DATE_FORMAT = '%d.%m.%Y'
DATE_DIVIDER = '-'


def parse_date(date_str):
    parsed_date = datetime.strptime(date_str, DATE_FORMAT)
    return parsed_date


def get_date_range(date_str):

    start, *rest = date_str.split(DATE_DIVIDER)
    end = rest[0] if rest else start
    start_date, end_date = map(parse_date, [start, end])

    return start_date, end_date


def is_available_date(booked_dates, date_for_booking):

    start_date_for_booking, end_date_for_booking = get_date_range(date_for_booking)

    idx = 0
    is_available = True

    while is_available and idx < len(booked_dates):
        
        start_booked_date, end_booked_date = get_date_range(booked_dates[idx])
        is_available =  (start_date_for_booking > end_booked_date and end_date_for_booking > end_booked_date) or \
                        (start_date_for_booking < end_booked_date and  end_date_for_booking < start_booked_date)
        idx += 1

    return is_available


def main():

    dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
    some_date = '10.11.2021-14.11.2021'
    print(is_available_date(dates, some_date))


main()