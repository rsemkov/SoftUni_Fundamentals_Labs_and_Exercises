def plunder(the_town, the_people, the_gold, the_dict):
    # Executes the Plunder action
    the_dict[the_town][0] -= the_people
    the_dict[the_town][1] -= the_gold
    print(f"{the_town} plundered! {the_gold} gold stolen, {the_people} citizens killed.")
    if the_dict[the_town][0] <= 0 or the_dict[the_town][1] <= 0:
        del the_dict[the_town]
        print(f"{the_town} has been wiped off the map!")
    return the_dict


def prosper(the_town, the_gold, the_dict):
    # Executes the Prosper action
    if the_gold >= 0:
        the_dict[the_town][1] += the_gold
        print(f"{the_gold} gold added to the city treasury. {the_town} now has {the_dict[the_town][1]} gold.")
    else:
        print("Gold added cannot be a negative number!")
    return the_dict


def data_collector(the_dict):
    # Fills the initial empty dict with the initial data
    while True:
        command = input()
        if command == "Sail":
            break
        command = command.split("||")
        city = command[0]
        population, gold = int(command[1]), int(command[2])
        if city not in the_dict.keys():
            the_dict[city] = [0, 0]
        the_dict[city][0] += population
        the_dict[city][1] += gold
    return the_dict


def operator(the_dict):
    # Conducts the operations based on the different actions entered in the input
    while True:
        command_input = input()
        if command_input == "End":
            break
        command_input = command_input.split("=>")
        action = command_input[0]
        town = command_input[1]
        if action == "Plunder":
            people = int(command_input[2])
            gold_coins = int(command_input[3])
            cities_dict = plunder(town, people, gold_coins, towns_data_dict)
        elif action == "Prosper":
            gold_coins = int(command_input[2])
            cities_dict = prosper(town, gold_coins, towns_data_dict)
    return the_dict


def printer(the_dict):
    # Prints the end results
    if the_dict:
        cities_count = len(the_dict)
        print(f"Ahoy, Captain! There are {cities_count} wealthy settlements to go to:")
        for town, data in the_dict.items():
            populations = data[0]
            gold_pieces = data[1]
            print(f"{town} -> Population: {populations} citizens, Gold: {gold_pieces} kg")
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


towns_data_dict = {}
towns_data_dict = data_collector(towns_data_dict)
towns_data_dict = operator(towns_data_dict)
printer(towns_data_dict)
