import re
str_input = [x.strip() for x in input().split(",")]
winning_pattern = r"[@#\$\^]{6,9}"
winning_symbols = ['@', '#', '$', '^']

for current_ticket in str_input:
    outcome = "no match"
    uninterrupted_chars = 0
    if len(current_ticket) == 20:
        if len(set(current_ticket)) == 1 and current_ticket[0] in winning_symbols:
            outcome = "jackpot"
        else:
            first_half = current_ticket[:10]
            second_half = current_ticket[10:]
            match_one = re.findall(winning_pattern, first_half)
            match_two = re.findall(winning_pattern, second_half)
            if match_one:
                matches_one = [x for x in match_one[0]]
                matches_two = [y for y in match_two[0]]
                if matches_one[0] == matches_two[0]:
                    outcome = "winning"
                    uninterrupted_chars = min(len(matches_one), len(matches_two))
    else:
        outcome = "invalid"

    if outcome == "invalid":
        print('invalid ticket')
    elif outcome == "no match":
        print(f'ticket "{current_ticket}" - no match')
    elif outcome == "winning":
        print(f'ticket "{current_ticket}" - {uninterrupted_chars}{matches_one[0]}')
    elif outcome == "jackpot":
        print(f'ticket "{current_ticket}" - {10}{current_ticket[0]} Jackpot!')
