from datetime import datetime, timedelta


DATE_FORMAT = '%d.%m.%Y'
DATE_DIVIDER = '-'


def parse_date(date_str):
    parsed_date = datetime.strptime(date_str, DATE_FORMAT)
    return parsed_date


def is_booked(date, booked_ranges):
    is_booked = False

    for booked_range in booked_ranges:
        
        if DATE_DIVIDER in booked_range:
            start, end = booked_range.split(DATE_DIVIDER)
            start_date = parse_date(start)
            end_date = parse_date(end)
            
            if start_date <= date <= end_date:
                is_booked = True
        else:
            if parse_date(booked_range) == date:
                is_booked = True
                
    return is_booked


def is_available_date(booked_dates, date_for_booking):
    
    # Divide the date for booking into a period, if necessary
    if DATE_DIVIDER in date_for_booking:
        start, end = date_for_booking.split(DATE_DIVIDER)
        start_date = parse_date(start)
        end_date = parse_date(end)
        booking_dates = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]
    else:
        booking_dates = [parse_date(date_for_booking)]

    # Check each booking date
    are_free_dates = True
    for booking_date in booking_dates:
        if is_booked(booking_date, booked_dates):
            are_free_dates = False
            break
    
    return are_free_dates
