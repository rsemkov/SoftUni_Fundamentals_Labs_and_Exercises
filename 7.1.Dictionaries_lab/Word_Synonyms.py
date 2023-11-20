n = int(input())

my_dict = {}
for _ in range(n):
    key_input = input()
    value_input = input()

# CHECKS IF THERE IS ALREADY SUCH KEY. IF THERE IS, IT JUST ADDS MORE VALUES TO THE ALREADY EXISTING KEY
    if key_input not in my_dict:
        my_dict[key_input] = value_input
    else:
        my_dict[key_input] += f", {value_input}"

# THIS WILL UNPACK THE ITEMS
for key, value in my_dict.items():
    print(f"{key} - {value}")
