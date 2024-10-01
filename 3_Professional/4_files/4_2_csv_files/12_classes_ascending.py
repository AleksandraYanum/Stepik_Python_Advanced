# TODO: 
# 1. streaming processing: line by line
# 2. extract classes in func

from csv import DictReader, DictWriter


YEAR_COL_NAME = 'year'
CLASS_DELIMITER = '-'


# Extract and sort class names from the first row
def extract_sorted_classes(row, year_col_name=YEAR_COL_NAME, class_delimiter=CLASS_DELIMITER):

    sorted_classes= sorted(row.keys() - {year_col_name}, 
                  key=lambda x: (int(x.split(class_delimiter)[0]), x.split(class_delimiter)[1]))
    return sorted_classes


# Create a sorted row based on the classes' names
def create_sorted_row(row, classes, year_col_name=YEAR_COL_NAME):
    sorted_row = {year_col_name: row[year_col_name]}
    sorted_row.update({cls: row[cls] for cls in classes})
    return sorted_row


def sorted_student_counts(input_file, output_file):

    with open(input_file, encoding='utf-8') as file:

        reader = DictReader(file)

        first_row = next(reader)
        classes = extract_sorted_classes(first_row)
        sorted_headers = [YEAR_COL_NAME] + classes

        with open(output_file, 'w', encoding='utf-8', newline='') as file:

            writer = DictWriter(file, fieldnames=sorted_headers)
            writer.writeheader()

            # Process the first row
            sorted_row = create_sorted_row(first_row, classes)
            writer.writerow(sorted_row)

            # Process the rest of the rows
            for row in reader:
                sorted_row = create_sorted_row(row, classes)
                writer.writerow(sorted_row)


def main():
    sorted_student_counts('student_counts.csv', 'sorted_student_counts.csv')


main()