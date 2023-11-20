wagons_count = int(input())

train = [int(0) for _ in range(wagons_count)]

while True:
    command = input().split()
    if command[0] == "End":
        break

    elif command[0] == "add":
        people_to_add = int(command[1])
        train[-1] += people_to_add

    elif command[0] == "insert":
        insert_index = int(command[1])
        train[insert_index] += int(command[2])

    elif command[0] == "leave":
        remove_index = int(command[1])
        train[remove_index] = int(train[remove_index]) - int(command[2])

print(train)