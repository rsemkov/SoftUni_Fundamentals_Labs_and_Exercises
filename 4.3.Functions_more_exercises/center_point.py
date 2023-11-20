import math


def distance_to_center(x, y):
    distance = math.sqrt(x ** 2 + y ** 2)
    return distance


def int_converter(a, b):
    a, b = math.floor(a), math.floor(b)
    return f"({a}, {b})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

distance_1 = distance_to_center(x1, y1)
distance_2 = distance_to_center(x2, y2)
if distance_1 <= distance_2:
    print(int_converter(x1, y1))
else:
    print(int_converter(x2, y2))
