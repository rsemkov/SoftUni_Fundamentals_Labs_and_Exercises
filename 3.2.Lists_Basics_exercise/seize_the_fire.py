fires_and_cells = input().split("#")
water = int(input())

total_effort = 0
total_fire = 0
cells_list = []

for i in fires_and_cells:
    i = i.split(" = ")
    fire_level = i[0]
    fire_value = int(i[1])

    if (fire_level == "High" and (fire_value < 81 or fire_value > 125)) or \
       (fire_level == "Medium" and (fire_value < 51 or fire_value > 80)) or \
       (fire_level == "Low" and (fire_value < 1 or fire_value > 50)):
        continue

    if water < fire_value:
        continue

    water -= fire_value
    total_effort += fire_value * 0.25
    total_fire += fire_value
    cells_list.append(fire_value)

print("Cells:")

for cell in cells_list:
    print("- " + str(cell))

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")







