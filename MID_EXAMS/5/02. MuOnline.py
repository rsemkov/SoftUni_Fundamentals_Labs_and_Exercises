string_input = [_ for _ in input().split("|")]

initial_health = 100
initial_bitcoins = 0

room_reached = 0
failed_quest = False
for room in string_input:
    room_reached += 1
    room = room.split()
    command = room[0]
    number = int(room[1])

    if command == "potion":
        if initial_health + number > 100:
            hp_healed = 100 - initial_health
        else:
            hp_healed = number

        initial_health += hp_healed
        print(f"You healed for {hp_healed} hp.")
        print(f"Current health: {initial_health} hp.")

    elif command == "chest":
        bitcoins_found = number
        initial_bitcoins += bitcoins_found

        print(f"You found {bitcoins_found} bitcoins.")

    else:  # monster
        monster_type = command
        monster_attack = number
        initial_health -= monster_attack

        if initial_health > 0:
            print(f"You slayed {monster_type}.")
        else:
            failed_quest = True
            print(f"You died! Killed by {monster_type}.")
            print(f"Best room: {room_reached}")
            break

if not failed_quest:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")
