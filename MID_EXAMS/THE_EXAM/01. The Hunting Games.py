adventure_days = int(input())
players_count = int(input())
group_energy = float(input())
daily_water_per_person = float(input())
daily_food_per_person = float(input())

total_food = daily_food_per_person * players_count * adventure_days
total_water = daily_water_per_person * players_count * adventure_days

quest_succeeded = True
for day in range(1 , adventure_days + 1):
    energy_loss = float(input())
    if group_energy <= energy_loss:
        quest_succeeded = False
        break

    group_energy -= energy_loss

    if day % 2 == 0:
        group_energy *= 1.05
        total_water *= 0.7
    if day % 3 == 0:
        group_energy *= 1.1
        total_food -= total_food / players_count

if quest_succeeded:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")