import csv
from collections import defaultdict


TOTAL_SALARY = 'total_salary'
EMPLOYEE_AMOUNT = 'count'
COMPANY_NAME_COL_NAME = 'company_name'
SALARY_COL_NAME = 'salary'
DELIMITER_SYM = ';'


# Словарь для хранения сумм зарплат и количества сотрудников для каждой компании
company_data = defaultdict(lambda: {TOTAL_SALARY: 0, EMPLOYEE_AMOUNT: 0})

with open('salary_data.csv', encoding='utf-8') as csv_file:
    salary_data = csv.DictReader(csv_file, delimiter=DELIMITER_SYM)
    
    for row in salary_data:
        company_name = row[COMPANY_NAME_COL_NAME]
        salary = int(row[SALARY_COL_NAME])
        company_data[company_name][TOTAL_SALARY] += salary
        company_data[company_name][EMPLOYEE_AMOUNT] += 1

average_salaries = [
    (company, data[TOTAL_SALARY] / data[EMPLOYEE_AMOUNT])
    for company, data in company_data.items() if data[EMPLOYEE_AMOUNT] > 0
]

sorted_companies = sorted(average_salaries, key=lambda x: (x[1], x[0]))

for company, _ in sorted_companies:
    print(company)