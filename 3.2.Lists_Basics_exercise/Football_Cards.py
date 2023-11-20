cards_sequence = input()

players_count_a = 11
players_count_b = 11
game_terminated = False

cards_list = set(cards_sequence.split())

for player in cards_list:
    if "A" in player:
        players_count_a -= 1
    else:
        players_count_b -= 1

    if players_count_a < 7 or players_count_b < 7:
        game_terminated = True
        break

print(f"Team A - {players_count_a}; Team B - {players_count_b}")
if game_terminated:
    print("Game was terminated")

