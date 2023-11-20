def register(the_name, the_license, registry):
    if the_name in registry.keys():
        print(f"ERROR: already registered with plate number {the_license}")
    else:
        registry[the_name] = the_license
        print(f"{the_name} registered {the_license} successfully")
    return registry


def unregister(the_name, registry):
    if the_name not in registry.keys():
        print(f"ERROR: user {the_name} not found")
    else:
        del registry[the_name]
        print(f"{the_name} unregistered successfully")
    return registry


def main():
    cars_count = int(input())
    car_registry = {}

    for _ in range(cars_count):
        command = input().split()
        username = command[1]
        if command[0] == "register":
            license_plate_number = command[2]
            car_registry = register(username, license_plate_number, car_registry)
        elif command[0] == "unregister":
            car_registry = unregister(username, car_registry)

    for user, plate in car_registry.items():
        print(f"{user} => {plate}")


main()
