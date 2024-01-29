STUDENT_AMOUNT = 3

student_1, student_2, student_3 = [set([int(i) for i in input().split()]) for n in range(STUDENT_AMOUNT)]

found_in_all_students = student_1.intersection(student_2, student_3)
found_in_no_more_than_2_students_sorted = sorted(student_1.union(student_2, student_3).
                                                           difference(found_in_all_students))

print(*found_in_no_more_than_2_students_sorted)