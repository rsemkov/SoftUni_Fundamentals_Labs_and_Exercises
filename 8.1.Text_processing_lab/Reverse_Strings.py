while True:
    command = input()
    if command == "end":
        break

    word = command
    reversed_word = command[::-1]
    print(f"{word} = {reversed_word}")

