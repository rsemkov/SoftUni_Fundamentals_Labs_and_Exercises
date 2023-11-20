def abs_values(input_list):
    result_list = [abs(x) for x in input_list]
    return result_list


nums_input = list(map(float, input().split()))
print(abs_values(nums_input))
