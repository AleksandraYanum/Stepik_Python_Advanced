STUDENT_AMOUNT = 3

student_1, student_2, student_3 = [set([int(i) for i in input().split()]) for n in range(STUDENT_AMOUNT)]

student_3_dif_sorted = sorted(student_3.difference(student_1, student_2), reverse=True)

print(*student_3_dif_sorted)