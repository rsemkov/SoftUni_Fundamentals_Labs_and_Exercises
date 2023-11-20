def sign_checker(num_1, num_2, num_3):
    nums_list = [num_1, num_2, num_3]
    positive_list = list(filter(lambda x: x > 0, nums_list))

    if 0 in nums_list:
        return "zero"
    elif len(positive_list) == 1 or len(positive_list) == 3:
        return "positive"
    else:
        return "negative"


num_1_input = int(input())
num_2_input = int(input())
num_3_input = int(input())

print(sign_checker(num_1_input, num_2_input, num_3_input))



