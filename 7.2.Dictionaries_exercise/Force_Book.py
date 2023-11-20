force_book = {}


def add_users(side, user, the_dict):
    if side not in the_dict.keys():
        the_dict[side] = []
    add_user = True
    for sides, users in the_dict.items():
        if user in users:
            add_user = False
    if add_user:
        the_dict[side].append(user)
    return the_dict


def change_side(side, user, the_dict):
    if side not in the_dict.keys():
        the_dict[side] = []
    for sides, users in the_dict.items():
        if user in users:
            idx = users.index(user)
            del the_dict[sides][idx]
    the_dict[side].append(user)
    print(f"{user} joins the {side} side!")
    return the_dict


while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if " | " in command:
        force_side, force_user = command.split(" | ")
        force_book = add_users(force_side, force_user, force_book)
    else:
        force_user, force_side = command.split(" -> ")
        force_book = change_side(force_side, force_user, force_book)

for key, value in force_book.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for force_user in value:
            print(f"! {force_user}")
