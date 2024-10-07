from csv import DictReader, DictWriter
from collections import defaultdict


ITEM_COL_NAME = 'item'
PROPERTY_COL_NAME = 'property'
VALUE_COL_NAME = 'value'


def condense_csv(file_name, id_name):
    # Dictionary {object: {property: value}}
    item_data = defaultdict(dict)

    with open(file_name, encoding='utf-8') as file:
        reader = DictReader(file, fieldnames=[ITEM_COL_NAME, PROPERTY_COL_NAME, VALUE_COL_NAME])
        for row in reader:
            item = row[ITEM_COL_NAME]
            property = row[PROPERTY_COL_NAME]
            value = row[VALUE_COL_NAME]
            item_data[item][property] = value
    
    property_list = list(item_data.values())[0].keys()

    with open('condensed.csv', 'w', encoding='utf-8', newline='') as file:
        writer = DictWriter(file, fieldnames=[id_name] + property_list)
        writer.writeheader()

        for item in sorted(item_data):
            item_row = {id_name: item}
            item_row.update(item_data[item])
            writer.writerow(item_row) 