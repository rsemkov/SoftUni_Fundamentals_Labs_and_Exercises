first_employee_per_hour = int(input())
second_employee_per_hour = int(input())
third_employee_per_hour = int(input())
students_count = int(input())

total_per_hour = first_employee_per_hour + second_employee_per_hour + third_employee_per_hour

hours_counter = 0
extra_hours_counter = 0

while students_count > 0:
    hours_counter += 1
    students_count -= total_per_hour

    if hours_counter % 3 == 0 and students_count > 0:
        extra_hours_counter += 1

total_hours = hours_counter + extra_hours_counter

print(f"Time needed: {total_hours}h.")

