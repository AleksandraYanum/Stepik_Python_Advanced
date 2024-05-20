from sys import stdin
from datetime import date

def main():
    сurr_date = date.fromisoformat(stdin.readline().strip())
    min_date, max_date = сurr_date, сurr_date

    for line in stdin:
        curr_date = date.fromisoformat(line.strip())
        if curr_date > max_date:
            max_date = curr_date
        elif curr_date < min_date:
            min_date = curr_date

    max_min_delta = (max_date - min_date).days

    print(max_min_delta)


main()