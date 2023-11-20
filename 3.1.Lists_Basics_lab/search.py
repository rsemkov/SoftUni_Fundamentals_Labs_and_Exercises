n = int(input())
word = input()

list = []
list_with_the_word = []

for _ in range(n):
    commands = input()
    list.append(commands)

    if word in commands:
        list_with_the_word.append(commands)

print(list)
print(list_with_the_word)


