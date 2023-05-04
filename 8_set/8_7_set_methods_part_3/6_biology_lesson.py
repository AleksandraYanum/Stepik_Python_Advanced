ALL_POSSIBLE_MARKS = set(range(11))
STUDENT_AMOUNT = 3

student_1, student_2, student_3 = [set([int(i) for i in input().split()]) for n in range(STUDENT_AMOUNT)]

all_student_marks = student_1.union(student_2, student_3)
not_found_marks = ALL_POSSIBLE_MARKS.difference(all_student_marks)

print(*sorted(not_found_marks))
