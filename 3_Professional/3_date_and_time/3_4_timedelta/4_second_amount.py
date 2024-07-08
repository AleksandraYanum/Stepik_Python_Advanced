from datetime import timedelta

INPUT_DIVIDER = ':'


hours, minutes, seconds = map(int, input().split(INPUT_DIVIDER))
time_delta_seconds = int(timedelta(hours=hours, minutes=minutes, seconds=seconds).total_seconds())

print(time_delta_seconds)
