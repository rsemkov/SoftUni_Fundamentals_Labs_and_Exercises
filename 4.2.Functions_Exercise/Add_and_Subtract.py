def sum_numbers(num1, num2):
    return num1 + num2


def subtract(result, num3):
    return result - num3


def add_and_subtract(num1, num2, num3):
    added_nums = sum_numbers(num1, num2)
    result = subtract(added_nums, num3)
    return result


num1_input = int(input())
num2_input = int(input())
num3_input = int(input())

print(add_and_subtract(num1_input, num2_input, num3_input))
