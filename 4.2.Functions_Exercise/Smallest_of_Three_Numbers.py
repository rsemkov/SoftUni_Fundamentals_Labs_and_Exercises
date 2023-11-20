num1_input = int(input())
num2_input = int(input())
num3_input = int(input())


def smallest_num(num1, num2, num3):
    nums_list = [num1, num2, num3]
    return min(nums_list)


print(smallest_num(num1_input, num2_input, num3_input))