resource = input()
resources_dict = {}

while resource != "stop":
    quantity = int(input())
    if resource not in resources_dict.keys():
        resources_dict[resource] = 0
    resources_dict[resource] += quantity

    resource = input()

for resource, quantity in resources_dict.items():
    print(f"{resource} -> {quantity}")