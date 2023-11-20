n = int(input())

for _ in range(n):
    string = input()
    pure = True

    for letter in string:
        if letter == "." or letter == "," or letter == "_":
            print(f"{string} is not pure!")
            pure = False
            break
    if pure:
        print(f"{string} is pure.")


