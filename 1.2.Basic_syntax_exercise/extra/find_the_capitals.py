string = input()

list =[]
for index, letter in enumerate(string):
    if letter.isupper():
        list.append(index)

print(list)
