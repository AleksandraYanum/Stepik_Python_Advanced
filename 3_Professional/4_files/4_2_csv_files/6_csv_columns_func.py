from csv import DictReader
from collections import defaultdict


def csv_columns(filename):

    column_value_dict = defaultdict(list)

    with open(filename, encoding='utf-8') as file:
        rows = DictReader(file)
               
        for row in rows:
            for header in rows.fieldnames:
                column_value_dict[header].append(row[header])

    return dict(column_value_dict)