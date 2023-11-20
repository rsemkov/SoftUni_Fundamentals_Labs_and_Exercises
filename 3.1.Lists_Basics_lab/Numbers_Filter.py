n = int(input())

list = []
list_2 = []
for _ in range(n):
    number = int(input())
    list.append(number)

command = input()

if command == "even":
    for i in list:
        if i % 2 == 0:
            list_2.append(i)

elif command == "odd":
    for i in list:
        if i % 2 != 0:
            list_2.append(i)

elif command == "negative":
    for i in list:
        if i < 0:
            list_2.append(i)

elif command == "positive":
    for i in list:
        if i >= 0:
            list_2.append(i)

print(list_2)