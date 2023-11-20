def tic_tac_toe_result(line_1, line_2, line_3, player):
    player_won = False

    # this checks if there is a vertical match:
    for index in range(3):
        if line_1[index] == line_2[index] == line_3[index] == player:
            player_won = True

    # this checks if there is a horizontal match:
    if (line_1[0] == line_1[1] == line_1[2] == player) or \
       (line_2[0] == line_2[1] == line_2[2] == player) or \
       (line_3[0] == line_3[1] == line_3[2] == player):
        player_won = True

    # this checks if there is an "X" kind of match:
    if (line_1[0] == line_2[1] == line_3[2] == player) or \
       (line_1[2] == line_2[1] == line_3[0] == player):
        player_won = True

    return player_won


line_1_input = input().split()
line_2_input = input().split()
line_3_input = input().split()

# checks if any of the players won:
result_player_1 = tic_tac_toe_result(line_1_input, line_2_input, line_3_input, "1")
result_player_2 = tic_tac_toe_result(line_1_input, line_2_input, line_3_input, "2")

if result_player_1:
    print("First player won")
elif result_player_2:
    print("Second player won")
else:
    print("Draw!")


