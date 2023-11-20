friends_list = input().split(", ")
blacklisted_names = 0
lost_names = 0


def blacklist(the_name, the_list):
    global blacklisted_names
    if the_name not in the_list:
        print(f"{the_name} was not found.")
    else:
        blacklisted_names += 1
        for index, names in enumerate(the_list):
            if names == the_name:
                the_list[index] = "Blacklisted"
                print(f"{the_name} was blacklisted.")
    return the_list


def error(index, the_list):
    global lost_names
    if 0 <= index < len(the_list):
        if the_list[index] != "Blacklisted" and the_list[index] != "Lost":
            print(f"{the_list[index]} was lost due to an error.")
            the_list[index] = "Lost"
            lost_names += 1
    return the_list


def change(index, the_new_name, the_list):
    if 0 <= index < len(the_list):
        print(f"{the_list[index]} changed his username to {the_new_name}.")
        the_list[index] = the_new_name
    return the_list


while True:
    command = input()
    if command == "Report":
        break
    command = command.split()
    action = command[0]

    if action == "Blacklist":
        name = command[1]
        friends_list = blacklist(name, friends_list)
    elif action == "Error":
        idx = int(command[1])
        friends_list = error(idx, friends_list)
    elif action == "Change":
        idx = int(command[1])
        new_name = command[2]
        friends_list = change(idx, new_name, friends_list)


print(f"Blacklisted names: {blacklisted_names}")
print(f"Lost names: {lost_names}")
print(" ".join(friends_list))

