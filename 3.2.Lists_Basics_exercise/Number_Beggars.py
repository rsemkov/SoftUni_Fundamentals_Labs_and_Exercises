str_input = input().split(", ")
beggars_count = int(input())

list_of_sums = []

for beggar in range(beggars_count):
    current_sum = 0
    for index in range(beggar, len(str_input), beggars_count):
        current_sum += int(str_input[index])

    list_of_sums.append(current_sum)

print(list_of_sums)


