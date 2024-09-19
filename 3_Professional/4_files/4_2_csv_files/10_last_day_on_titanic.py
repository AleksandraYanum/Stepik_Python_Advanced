from csv import DictReader


DELIMITER_CSV = ';'
IS_SURVIVED_CSV = 'survived'
NAME_CSV = 'name'
SEX_CSV = 'sex'
AGE_CSV = 'age'
IS_SURVIVED = '1'
MALE = 'male'
MATURITY_AGE = 18


with open('titanic.csv', 'r', encoding='utf-8') as file:

    titanic_passengers = DictReader(file, delimiter=DELIMITER_CSV)
    males = []
    females = []
    
    for row in titanic_passengers:
        if row[IS_SURVIVED_CSV] == IS_SURVIVED and row[AGE_CSV] and float(row[AGE_CSV]) < MATURITY_AGE:
            if row[SEX_CSV] == MALE:
                males.append(row[NAME_CSV])
            else:
                females.append(row[NAME_CSV])
    
    for name in males:
        print(name)
    for name in females:
        print(name)