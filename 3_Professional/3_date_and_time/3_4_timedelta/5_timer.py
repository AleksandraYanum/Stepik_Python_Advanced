from datetime import datetime, timedelta

TIME_PATTERN = '%H:%M:%S'


current_time = datetime.strptime(input(), TIME_PATTERN)
timer_seconds = int(input()) 
timer_time = current_time + timedelta(seconds=timer_seconds)

print(timer_time.strftime(TIME_PATTERN))
