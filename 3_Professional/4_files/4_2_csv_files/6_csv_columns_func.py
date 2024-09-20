from csv import reader

def csv_columns(filename):
    with open(filename, encoding='utf-8') as file:
        rows = reader(file)
        headers = next(rows)
        
        columns = {header: [] for header in headers}
        
        for row in rows:
            for header, value in zip(headers, row):
                columns[header].append(value)
                
    return columns