import sys
import math
number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

# THIS ELIMINATES A DIVISION BY 0 SCENARIO:
if number_of_lectures == 0:
    print(f"Max Bonus: 0.")
    print(f"The student has attended 0 lectures.")

# COVERS ALL OTHER CASES APART FROM DIVISION BY 0 CASE:
else:
    max_bonus = -sys.maxsize
    max_attendances = -sys.maxsize

    for _ in range(number_of_students):
        count_of_attendances_per_student = int(input())
        total_bonus_per_student = count_of_attendances_per_student / number_of_lectures * (5 + additional_bonus)

        if total_bonus_per_student > max_bonus:
            max_bonus = total_bonus_per_student
            max_attendances = count_of_attendances_per_student

    print(f"Max Bonus: {math.ceil(max_bonus)}.")
    print(f"The student has attended {math.ceil(max_attendances)} lectures.")
