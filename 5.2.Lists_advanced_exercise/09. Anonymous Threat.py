def merge(start_index, stop_index, the_list):
    if start_index < 0:
        start_index = 0
    elif start_index > len(the_list) - 1:
        start_index = len(the_list) - 1

    if stop_index < 0:
        stop_index = 0
    elif stop_index > len(the_list) - 1:
        stop_index = len(the_list) - 1

    the_list[start_index: stop_index + 1] = ["".join(the_list[start_index: stop_index + 1])]
    return the_list


def divide(index, partitions_count, the_list):
    chars_per_item = len(the_list[index]) // partitions_count
    the_list[index] = []




initial_input = input().split()
while True:
    command = input()
    if command == "3:1":
        break
    command = command.split()
    action = command[0]

    if action == "merge":
        start, stop = int(command[1]), int(command[2])
        initial_input = merge(start, stop, initial_input)
    elif action == "divide":
        idx, partitions = int(command[1]), int(command[2])


print(" ".join(initial_input))