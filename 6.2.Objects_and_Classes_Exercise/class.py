class Class:
    __students_count = 22
    students = []
    grades = []

    def __init__(self, name):
        self.name = name

    def add_student(self, name: str, grade: float):
        if len(Class.students) < 22:
            Class.students.append(name)
            Class.grades.append(grade)

    def get_average_grade(self):
        average_grade = sum(Class.grades) / len(Class.grades)
        return average_grade

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {sum(Class.grades)/len(Class.grades):.2f}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)