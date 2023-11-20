initial_list = [int(x) for x in input().split("@")]

current_position = 0
while True:
    command = input()
    if command == "Love!":
        break
    command = command.split()

    jump_length = int(command[1])

    current_position += jump_length
# THIS RESETS HIS CURRENT POSITION IF IT GOES BEYOND THE LAST INDEX
    if current_position >= len(initial_list):
        current_position = 0

    if initial_list[current_position] == 0:
        print(f"Place {current_position} already had Valentine's day.")
        continue

    initial_list[current_position] -= 2

    if initial_list[current_position] == 0:
        print(f"Place {current_position} has Valentine's day.")

failed_houses_list = []
for house in initial_list:
    if house != 0:
        failed_houses_list.append(house)

failed_houses = len(failed_houses_list)

print(f"Cupid's last position was {current_position}.")
if failed_houses == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {failed_houses} places.")



