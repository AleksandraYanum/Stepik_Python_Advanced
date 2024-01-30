student_1, student_2, student_3 = set(int(i) for i in input().split()), \
    set(int(i) for i in input().split()), \
    set(int(i) for i in input().split())

student_1_2_dif_3_sorted = sorted(student_1.intersection(student_2).
                                            difference(student_3), reverse=True)

print(*student_1_2_dif_3_sorted)
