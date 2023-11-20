initial_values = [int(x) for x in input().split()]

while True:
    command = input()
    if command == "end":
        break
    command = command.split()
    action = command[0]

    if action == "swap":
        index1 = int(command[1])
        index2 = int(command[2])
        initial_values[index1], initial_values[index2] = initial_values[index2], initial_values[index1]

    elif action == "multiply":
        index1 = int(command[1])
        index2 = int(command[2])
        initial_values[index1] = initial_values[index1] * initial_values[index2]

    else:   # action == "decrease"
        for index in range(len(initial_values)):
            initial_values[index] -= 1

initial_values = [str(i) for i in initial_values]
print(", ".join(initial_values))
