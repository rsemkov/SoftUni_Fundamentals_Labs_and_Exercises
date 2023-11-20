people_waiting = int(input())
current_state = [int(x) for x in input().split()]
WAGON_LIMIT = 4

total_wagons = len(current_state)

final_result = []

for index in range(total_wagons):
    current_wagon_state = current_state[index]

    if people_waiting <= 0:
        break

    people_onboarded = WAGON_LIMIT - current_wagon_state
    people_in_current_wagon = people_onboarded + current_wagon_state
    people_waiting -= people_onboarded

    final_result.append(people_in_current_wagon)

print(final_result)



