all_materials = {"shards": 0, "fragments": 0, "motes": 0}

legendary_obtained = False
while not legendary_obtained:
    materials_input = input().lower().split()
    for index in range(0, len(materials_input), 2):
        material = materials_input[index + 1]
        quantity = int(materials_input[index])
        if material not in all_materials.keys():
            all_materials[material] = 0
        all_materials[material] += quantity

        if all_materials["shards"] >= 250:
            all_materials["shards"] -= 250
            legendary_obtained = True
            print("Shadowmourne obtained!")
            break
        elif all_materials["fragments"] >= 250:
            all_materials["fragments"] -= 250
            legendary_obtained = True
            print("Valanyr obtained!")
            break
        elif all_materials["motes"] >= 250:
            all_materials["motes"] -= 250
            legendary_obtained = True
            print("Dragonwrath obtained!")
            break

for material, quantity in all_materials.items():
    print(f"{material}: {quantity}")




