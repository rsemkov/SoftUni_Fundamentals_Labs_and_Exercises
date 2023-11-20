contests_dict = {}
while True:
    command = input()
    if command == "end of contests":
        break
    command = command.split(":")
    key = command[0]
    value = command[1]
    contests_dict[key] = value
###############
results_dict = {}
while True:
    command_2 = input()
    if command_2 == "end of submissions":
        break
    command_2 = command_2.split("=>")

    contest = command_2[0]
    password = command_2[1]
    username = command_2[2]
    points = int(command_2[3])

    if contest not in contests_dict.keys():
        continue

    if not contests_dict[contest] == password:
        continue
########
    if username not in results_dict.keys():
        results_dict[username] = [contest, points]
    else:
        if contest in results_dict[username] and points > results_dict[username][1]:



print(results_dict)
