rows_count = int(input())
students_and_grades = {}
for _ in range(rows_count):
    student = input()
    grade = float(input())
    if student not in students_and_grades.keys():
        students_and_grades[student] = []
    students_and_grades[student].append(grade)


for student, grades in students_and_grades.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")
