my_dict = {}

while True:
    command = input()

    if command.islower():
        command = command.replace('_', ' ')
        break

    student_info_input = command.split(":")

    keys = f"{student_info_input[0]} - {student_info_input[1]}"
    values = student_info_input[2]

    # THIS ADDS THEM TO THE DICTIONARY:
    my_dict[keys] = values

for item in my_dict:
    if command in my_dict[item]:
        print(item)
