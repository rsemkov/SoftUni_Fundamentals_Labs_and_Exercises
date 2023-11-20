def min_num(list_for_smallest):
    list_for_smallest = min(list_for_smallest)
    return f"The minimum number is {list_for_smallest}"


def max_num(list_for_biggest):
    list_for_biggest = max(list_for_biggest)
    return f"The maximum number is {list_for_biggest}"


def sum_of_nums(list_for_sum):
    list_for_sum = sum(list_for_sum)
    return f"The sum number is: {list_for_sum}"


numbers_sequence = input().split()
numbers_sequence = [int(x) for x in numbers_sequence]


print(min_num(numbers_sequence))
print(max_num(numbers_sequence))
print(sum_of_nums(numbers_sequence))






