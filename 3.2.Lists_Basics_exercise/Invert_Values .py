str_input = input()

list = str_input.split( )

for i in range(0, len(list)):
    list[i] = int(list[i]) * -1

print(list)
