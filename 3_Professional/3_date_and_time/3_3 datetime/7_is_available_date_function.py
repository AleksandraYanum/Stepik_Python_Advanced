from datetime import datetime


DATE_FORMAT = '%d.%m.%Y'
DATE_DIVIDER = '-'


def parse_date(date_str):
    parsed_date = datetime.strptime(date_str, DATE_FORMAT)
    return parsed_date


def is_booked(start_date_for_booking, end_date_for_booking, booked_ranges):

    idx = 0
    is_booked = False

    while not is_booked and idx < len(booked_ranges):
        
        booked_dates = booked_ranges[idx].split(DATE_DIVIDER)
        start = booked_dates[0]
        end = booked_dates[1] if len(booked_dates) == 2 else start
        booked_start_date, booked_end_date = map(parse_date, [start, end])

        idx += 1

        if booked_start_date <= start_date_for_booking <= booked_end_date or \
           booked_start_date <= end_date_for_booking <= booked_end_date  or \
           start_date_for_booking <= booked_start_date <= end_date_for_booking:
                
                is_booked = True
                
    return is_booked


def is_available_date(booked_dates, date_for_booking):

    dates_for_booking = date_for_booking.split(DATE_DIVIDER)
    start = dates_for_booking[0]
    end = dates_for_booking[1] if len(dates_for_booking) == 2 else start
    start_date_for_booking, end_date_for_booking = map(parse_date, [start, end])

    is_available_date = not is_booked(start_date_for_booking, end_date_for_booking, booked_dates)

    return is_available_date



def main():

    dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
    some_date = '10.11.2021-14.11.2021'
    print(is_available_date(dates, some_date))


main()