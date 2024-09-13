import csv


DELIMITER_SYM = ';'
SURVIVED_POS = 0
NAME_POS = 1
SEX_POS = 2
AGE_POS = 3
SURVIVED_SYM = '1'
MALE_SYM = 'male'
MATURITY_AGE = 18


with open('titanic.csv', 'r', encoding='utf-8') as file:

    rows = csv.reader(file, delimiter=DELIMITER_SYM)
    next(rows)
    males = []
    females = []
    
    for row in rows:
        if row[SURVIVED_POS] == SURVIVED_SYM and row[AGE_POS] and float(row[AGE_POS]) < MATURITY_AGE:
            if row[SEX_POS] == MALE_SYM:
                males.append(row[NAME_POS])
            else:
                females.append(row[NAME_POS])
    
    for name in males:
        print(name)
    for name in females:
        print(name)