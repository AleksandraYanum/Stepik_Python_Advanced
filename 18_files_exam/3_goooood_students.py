MIN_GOOD_SCORE = 65


good_student_amount = 0

with open('grades.txt',  encoding='utf-8') as file:
    for line in file:
        name, *scores = line.split()
        if all(map(lambda x: True if x >= MIN_GOOD_SCORE else False, map(int, scores))):
                good_student_amount += 1

print(good_student_amount)