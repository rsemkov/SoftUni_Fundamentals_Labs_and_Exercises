str_input = input().split(", ")

zeros_list = list(filter(lambda x: x == "0", str_input))
no_zeros_list = list(filter(lambda x: x != "0", str_input))

result_list = no_zeros_list + zeros_list
result_list = [int(i) for i in result_list]

print(result_list)
