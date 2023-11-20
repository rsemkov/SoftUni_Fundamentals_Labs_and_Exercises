courses = {}
while True:
    data_input = input()
    if data_input == "end":
        break
    course_name, student_name = data_input.split(" : ")
    if course_name not in courses.keys():
        courses[course_name] = []
    courses[course_name].append(student_name)

for courses, students in courses.items():
    print(f"{courses}: {len(students)}")
    for student in students:
        print(f"-- {student}")
