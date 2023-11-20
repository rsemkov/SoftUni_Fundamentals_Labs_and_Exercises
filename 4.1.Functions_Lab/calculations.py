def calculator(num_1, num_2, operator):
    if operator == "multiply":
        return num_1 * num_2
    elif operator == "divide":
        return int(num_1 / num_2)
    elif operator == "add":
        return num_1 + num_2
    elif operator == "subtract":
        return num_1 - num_2


operator_input = input()
num_1_input = int(input())
num_2_input = int(input())
print(calculator(num_1_input, num_2_input, operator_input))



