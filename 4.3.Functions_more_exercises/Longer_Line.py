import math


def distance_to_center(x, y):
    # Calculates which of the 2 dots of a line is closer to the center:
    distance_center = math.sqrt(x ** 2 + y ** 2)
    return distance_center


def length_calculator(x_1, y_1, x_2, y_2):
    # calculates length of the line based on the coordinates of its 2 dots:
    length = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
    return length


def int_converter(a, b, c, d):
    # converts the data to the proper format:
    a, b, c, d = math.floor(a), math.floor(b), math.floor(c), math.floor(d)
    return f"({a}, {b})({c}, {d})"


def result_printer(a, b, c, d):
    # prints the result based on which of the two lines is longer:
    if distance_to_center(a, b) <= distance_to_center(c, d):
        return int_converter(a, b, c, d)
    else:
        return int_converter(c, d, a, b)


# takes the input of the 4 dots:
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())

# calculates which line is longer:
length_1 = length_calculator(x1, y1, x2, y2)
length_2 = length_calculator(a1, b1, a2, b2)

# calls the printing function to print the result:
if length_1 >= length_2:
    print(result_printer(x1, y1, x2, y2))
else:
    print(result_printer(a1, b1, a2, b2))
