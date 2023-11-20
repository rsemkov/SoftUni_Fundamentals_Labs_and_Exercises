target_sequence = [int(x) for x in input().split()]

shot_indexes_list = []
while True:
    command = input()
    if command == "End":
        break

    index = int(command)
# THIS PREVENTS SHOOTING THE SAME TARGET TWICE
    if index in shot_indexes_list:
        continue
# THIS REMOVES THE POSSIBILITY OF INVALID INDEX
    if index >= len(target_sequence):
        continue

    current_shot_target = target_sequence[index]
    target_sequence[index] = -1
    shot_indexes_list.append(index)

    for index in range(len(target_sequence)):
        if target_sequence[index] == -1:
            continue

        if target_sequence[index] > current_shot_target:
            target_sequence[index] -= current_shot_target
        else:
            target_sequence[index] += current_shot_target

target_sequence = [str(i) for i in target_sequence]
print(f"Shot targets: {len(shot_indexes_list)} -> {' '.join(target_sequence)}")
