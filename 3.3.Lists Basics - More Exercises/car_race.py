def result(player_list):
    result_list = []
    for index in range(len(player_list)):
        if player_list[index] != 0:
            result_list.append(player_list[index])
        else:
            the_sum = sum(result_list[:index]) * 0.8
            result_list[:index] = []
            result_list.append(the_sum)

    result_sum = sum(result_list)
    return result_sum


numbers_input = [int(x) for x in input().split()]
finishing_index = len(numbers_input) // 2

first_player = numbers_input[:finishing_index]
second_player = numbers_input[-1:finishing_index: -1]

result_first = result(first_player)
result_second = result(second_player)

if result_first <= result_second:
    print(f"The winner is left with total time: {result_first:.1f}")
else:
    print(f"The winner is right with total time: {result_second:.1f}")
