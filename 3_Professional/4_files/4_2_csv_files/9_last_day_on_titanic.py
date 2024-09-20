from csv import DictReader


DELIMITER_CSV = ';'
IS_SURVIVED_COL_NAME = 'survived'
NAME_COL_NAME = 'name'
SEX_COL_NAME = 'sex'
AGE_COL_NAME = 'age'
IS_SURVIVED = '1'
MALE = 'male'
MATURITY_AGE = 18


with open('titanic.csv', 'r', encoding='utf-8') as file:

    titanic_passengers = DictReader(file, delimiter=DELIMITER_CSV)
    males = []
    females = []
    
    for row in titanic_passengers:
        if row[IS_SURVIVED_COL_NAME] == IS_SURVIVED and float(row.get(AGE_COL_NAME, MATURITY_AGE)) < MATURITY_AGE:
            if row[SEX_COL_NAME] == MALE:
                males.append(row[NAME_COL_NAME])
            else:
                females.append(row[NAME_COL_NAME])
    
    for name in males:
        print(name)
    for name in females:
        print(name)