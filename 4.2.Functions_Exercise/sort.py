def sorted_list(list_of_nums):
    list_of_nums = [int(x) for x in list_of_nums]
    sorted_list_of_nums = sorted(list_of_nums)
    return sorted_list_of_nums


numbers_sequence = input().split()
print(sorted_list(numbers_sequence))
