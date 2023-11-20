sequence_input = input().split()

moves_done = 0
game_won = False
while True:
    command = input()
    if command == "end":
        break
    command = command.split()
    index_1 = int(command[0])
    index_2 = int(command[1])

    moves_done += 1

    # if they cheat:
    if index_1 == index_2 or (not len(sequence_input) > index_1 >= 0) or (not len(sequence_input) > index_2 >= 0):
        element_to_add = f"-{moves_done}a"
        sequence_input.insert(len(sequence_input) // 2, element_to_add)
        sequence_input.insert(len(sequence_input) // 2 + 1, element_to_add)
        print("Invalid input! Adding additional elements to the board")
        continue

    # if there is a match:
    if sequence_input[index_1] == sequence_input[index_2]:
        matched_element = sequence_input[index_1]
        if index_1 > index_2:
            sequence_input.pop(index_1)
            sequence_input.pop(index_2)
        else:
            sequence_input.pop(index_2)
            sequence_input.pop(index_1)
        print(f"Congrats! You have found matching elements - {matched_element}!")

    # if there is no match:
    else:
        print("Try again!")

    # if the game is won
    if len(sequence_input) == 0:
        game_won = True
        break

if game_won:
    print(f"You have won in {moves_done} turns!")
else:
    print("Sorry you lose :(")
    print(" ".join(sequence_input))
