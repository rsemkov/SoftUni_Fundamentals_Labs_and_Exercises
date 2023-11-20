the_list = [int(0) for x in range(12)]

while True:
    command = input().split("-")
    if command[0] == "End":
        break

    position = int(command[0]) - 1
    item = command[1]
    
    the_list.pop(position)
    the_list.insert(position, item)

while 0 in the_list:
    the_list.remove(0)

print(the_list)


