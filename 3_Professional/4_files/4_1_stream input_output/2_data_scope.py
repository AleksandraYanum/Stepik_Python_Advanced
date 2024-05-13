import sys
from datetime import datetime


dates = []

for line in sys.stdin:
    dates.append(datetime.fromisoformat(line.strip()))

max_min_delta = max(dates) - min(dates)
print(max_min_delta.days)
