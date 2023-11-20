import sys


def exchange(index, the_list):
    if index >= len(the_list) or index < 0:
        print("Invalid index")
    else:
        first_half = the_list[0: index + 1]
        second_half = the_list[index + 1::]
        the_list = second_half + first_half
    return the_list


def max_even_odd(even_odd, the_list):
    max_item = -sys.maxsize
    max_index = None
    if even_odd == "even":
        for index, item in enumerate(the_list):
            if item % 2 == 0 and item >= max_item:
                max_item = item
                max_index = index
    elif even_odd == "odd":
        for index, item in enumerate(the_list):
            if item % 2 != 0 and item >= max_item:
                max_item = item
                max_index = index
    if max_index is None:
        return "No matches"
    else:
        return max_index


def min_even_odd(even_odd, the_list):
    min_item = sys.maxsize
    min_index = None
    if even_odd == "even":
        for index, item in enumerate(the_list):
            if item % 2 == 0 and item <= min_item:
                min_item = item
                min_index = index
    elif even_odd == "odd":
        for index, item in enumerate(the_list):
            if item % 2 != 0 and item <= min_item:
                min_item = item
                min_index = index
    if min_index is None:
        return "No matches"
    else:
        return min_index


def first_even_odd(counter, even_odd, the_list):
    if count > len(the_list):
        return "Invalid count"
    if even_odd == "even":
        even_list = []
        counter = 0
        for num in the_list:
            if num % 2 == 0:
                even_list.append(num)
                counter += 1
            if counter >= count:
                break
        return even_list
    elif even_odd == "odd":
        odd_list = []
        counter = 0
        for num in the_list:
            if num % 2 != 0:
                odd_list.append(num)
                counter += 1
            if counter >= count:
                break
        return odd_list


def last_even_odd(counter, even_odd, the_list):
    if count > len(the_list):
        return "Invalid count"
    reversed_list = the_list[-1::-1]
    if even_odd == "even":
        even_list = []
        counter = 0
        for num in reversed_list:
            if num % 2 == 0:
                even_list.append(num)
                counter += 1
            if counter >= count:
                break
        return even_list[-1::-1]
    elif even_odd == "odd":
        odd_list = []
        counter = 0
        for num in reversed_list:
            if num % 2 != 0:
                odd_list.append(num)
                counter += 1
            if counter >= count:
                break
        return odd_list[-1::-1]


initial_input = [int(x) for x in input().split()]

while True:
    command = input()
    if command == "end":
        break
    command = command.split()
    action = command[0]

    if action == "exchange":
        idx = int(command[1])
        initial_input = exchange(idx, initial_input)

    elif action == "max":
        even_or_odd = command[1]
        print(max_even_odd(even_or_odd, initial_input))

    elif action == "min":
        even_or_odd = command[1]
        print(min_even_odd(even_or_odd, initial_input))

    elif action == "first":
        count = int(command[1])
        even_or_odd = command[2]
        print(first_even_odd(count, even_or_odd, initial_input))

    elif action == "last":
        count = int(command[1])
        even_or_odd = command[2]
        print(last_even_odd(count, even_or_odd, initial_input))

print(initial_input)
