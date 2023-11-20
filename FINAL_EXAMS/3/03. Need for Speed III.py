def drive(the_car, the_distance, the_fuel, the_dict):
    if the_dict[the_car][1] < the_fuel:
        print("Not enough fuel to make that ride")
    else:
        the_dict[the_car][1] -= the_fuel
        the_dict[the_car][0] += the_distance
        print(f"{the_car} driven for {the_distance} kilometers. {the_fuel} liters of fuel consumed.")
    if the_dict[the_car][0] >= 100000:
        print(f"Time to sell the {the_car}!")
        del the_dict[the_car]
    return the_dict


def refuel(the_car, the_fuel, the_dict):
    if the_dict[the_car][1] + the_fuel <= 75:
        fuel_loaded = the_fuel
    else:
        fuel_loaded = 75 - the_dict[the_car][1]
    the_dict[the_car][1] += fuel_loaded
    print(f"{the_car} refueled with {fuel_loaded} liters")
    return the_dict


def revert(the_car, km_reverted, the_dict):
    reverted = True
    the_dict[the_car][0] -= km_reverted
    if the_dict[the_car][0] < 10000:
        the_dict[the_car][0] = 10000
        reverted = False
    if reverted:
        print(f"{the_car} mileage decreased by {km_reverted} kilometers")
    return the_dict


def main():
    cars_count = int(input())
    cars_info = {}
    for _ in range(cars_count):
        current_car_data = input().split("|")
        car_name = current_car_data[0]
        mileage = int(current_car_data[1])
        fuel = int(current_car_data[2])
        if car_name not in cars_info.keys():
            cars_info[car_name] = []
        cars_info[car_name].append(mileage)
        cars_info[car_name].append(fuel)
    execute_main(cars_info)


def execute_main(the_dict):
    while True:
        command = input()
        if command == "Stop":
            break
        command = command.split(" : ")
        action = command[0]
        car = command[1]
        if action == "Drive":
            distance = int(command[2])
            fuel = int(command[3])
            cars_info = drive(car, distance, fuel, the_dict)
        elif action == "Refuel":
            fuel = int(command[2])
            cars_info = refuel(car, fuel, the_dict)
        elif action == "Revert":
            kilometres = int(command[2])
            cars_info = revert(car, kilometres, the_dict)
    print_fuc(the_dict)


def print_fuc(the_dict):
    for car, data in the_dict.items():
        car_mileage = data[0]
        car_fuel = data[1]
        print(f"{car} -> Mileage: {car_mileage} kms, Fuel in the tank: {car_fuel} lt.")


main()
