number = int(input())

biggest_number = [x for x in str(number)]

biggest_number.sort(reverse=True)

print("".join(biggest_number))