STUDENT_AMOUNT = 3

student_1, student_2, student_3 = [set([int(i) for i in input().split()]) for n in range(STUDENT_AMOUNT)]

all_student_marks = student_1.union(student_2, student_3)
found_in_all_students = student_1.intersection(student_2, student_3)
found_in_no_more_than_2_students = all_student_marks - found_in_all_students

print(*sorted(found_in_no_more_than_2_students))