electrons_count = int(input())

results_list = []
remaining_electrons = electrons_count

# this range is just the abs maximum range usable for every scenario
for index in range(1, electrons_count + 1):
    max_number = 2 * (index ** 2)
    if remaining_electrons >= max_number:
        remaining_electrons -= max_number
        results_list.append(max_number)
    else:
        # if the remaining electrons are 0, we do not add them, and just break the cycle. Otherwise, we add them and
        # break the cycle
        if remaining_electrons != 0:
            results_list.append(remaining_electrons)
        break

print(results_list)
