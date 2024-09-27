from csv import DictReader, DictWriter


YEAR_COL_NAME = 'year'
CLASS_DELIMITER = '-'


def sorted_student_counts(input_file, output_file):
    with open(input_file, encoding='utf-8') as file:
        reader = DictReader(file)
        data = [row for row in reader]  # list of dictionaries

    classes = sorted(data[0].keys() - {YEAR_COL_NAME}, 
                     key=lambda x: (int(x.split(CLASS_DELIMITER)[0]), x.split(CLASS_DELIMITER)[1]))
    sorted_headers = [YEAR_COL_NAME] + classes
    sorted_data = []

    for row in data:
        sorted_row = {YEAR_COL_NAME: row[YEAR_COL_NAME]}
        sorted_row.update({cls: row[cls] for cls in classes})
        sorted_data.append(sorted_row)

    with open(output_file, 'w', encoding='utf-8', newline='') as file:
        writer = DictWriter(file, fieldnames=sorted_headers)
        writer.writeheader()
        writer.writerows(sorted_data)


def main():
    sorted_student_counts('student_counts.csv', 'sorted_student_counts.csv')


main()