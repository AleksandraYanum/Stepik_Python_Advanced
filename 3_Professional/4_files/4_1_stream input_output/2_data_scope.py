from sys import stdin
from datetime import date

def main():

    min_date = date.max
    max_date = date.min

    for line in stdin:
        curr_date = date.fromisoformat(line.strip())
        if curr_date > max_date:
            max_date = curr_date
        if curr_date < min_date:
            min_date = curr_date

    max_min_delta = (max_date - min_date).days

    print(max_min_delta)


main()