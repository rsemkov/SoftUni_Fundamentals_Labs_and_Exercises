def rate(the_plant, the_rating, the_dict):
    if the_plant in the_dict.keys():
        the_dict[the_plant][1].append(the_rating)
    else:
        print("error")
    return the_dict


def update(the_plant, updated_rarity, the_dict):
    if the_plant in the_dict.keys():
        the_dict[the_plant][0] = updated_rarity
    else:
        print("error")
    return the_dict


def reset(the_plant, the_dict):
    if the_plant in the_dict.keys():
        the_dict[the_plant][1] = []
    else:
        print("error")
    return the_dict


n = int(input())
plants_dict = {}
for _ in range(n):
    plant_info = input().split("<->")
    plant_name = plant_info[0]
    plant_rarity = int(plant_info[1])
    plants_dict[plant_name] = [plant_rarity, []]

while True:
    command = input()
    if command == "Exhibition":
        break
    command = command.replace(" ", "")
    command = command.split(":")
    action = command[0]

    if action == "Rate":
        data = command[1].split("-")
        plant = data[0]
        rating = int(data[1])
        plants_dict = rate(plant, rating, plants_dict)
    elif action == "Update":
        data = command[1].split("-")
        plant = data[0]
        new_rarity = int(data[1])
        plants_dict = update(plant, new_rarity, plants_dict)
    elif action == "Reset":
        plant = command[1]
        plants_dict = reset(plant, plants_dict)

print("Plants for the exhibition:")
for plant, values in plants_dict.items():
    rarity = values[0]
    if len(values[1]) == 0:
        average_rating = 0
    else:
        average_rating = sum(values[1]) / len(values[1])
    print(f"- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")