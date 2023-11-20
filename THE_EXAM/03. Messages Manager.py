def add(the_user, sent, received, the_dict):
    if the_user not in the_dict.keys():
        the_dict[the_user] = [sent, received]
    return the_dict


def message(the_sender, the_receiver, capacity, the_dict):
    if the_sender in the_dict.keys() and the_receiver in the_dict.keys():
        the_dict[the_sender][0] += 1
        the_dict[the_receiver][1] += 1

        if sum(the_dict[the_sender]) >= capacity:
            print(f"{the_sender} reached the capacity!")
            del the_dict[the_sender]
        if sum(the_dict[the_receiver]) >= capacity:
            print(f"{the_receiver} reached the capacity!")
            del the_dict[the_receiver]
    return the_dict


def empty(the_user, the_dict):
    if the_user == "All":
        the_dict = {}
    else:
        del the_dict[the_user]
    return the_dict


def printer(the_dict):
    print(f"Users count: {len(the_dict)}")
    for user, messages in the_dict.items():
        total_messages = sum(messages)
        print(f"{user} - {total_messages}")


def main():
    total_capacity = int(input())
    data_dict = {}
    while True:
        command = input()
        if command == "Statistics":
            break
        command = command.split("=")
        action = command[0]
        if action == "Add":
            username = command[1]
            messages_sent = int(command[2])
            messages_received = int(command[3])
            data_dict = add(username, messages_sent, messages_received, data_dict)
        elif action == "Message":
            sender = command[1]
            receiver = command[2]
            data_dict = message(sender, receiver, total_capacity, data_dict)
        elif action == "Empty":
            username = command[1]
            data_dict = empty(username, data_dict)

    printer(data_dict)


main()
