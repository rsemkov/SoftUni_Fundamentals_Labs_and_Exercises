def add(the_piece, the_composer, the_key, the_dict):
    if the_piece not in the_dict.keys():
        the_dict[the_piece] = [the_composer, the_key]
        print(f"{the_piece} by {the_composer} in {the_key} added to the collection!")
    else:
        print(f"{the_piece} is already in the collection!")
    return the_dict


def remove(the_piece, the_dict):
    if the_piece in the_dict.keys():
        del the_dict[the_piece]
        print(f"Successfully removed {the_piece}!")
    else:
        print(f"Invalid operation! {the_piece} does not exist in the collection.")
    return the_dict


def change_key(the_piece, the_new_key, the_dict):
    if the_piece in the_dict.keys():
        the_dict[the_piece][1] = the_new_key
        print(f"Changed the key of {the_piece} to {the_new_key}!")
    else:
        print(f"Invalid operation! {the_piece} does not exist in the collection.")
    return the_dict


lines_count = int(input())
collection = {}
for _ in range(lines_count):
    data_input = input().split("|")
    piece = data_input[0]
    composer = data_input[1]
    key = data_input[2]
    collection[piece] = [composer, key]

while True:
    command = input()
    if command == "Stop":
        break
    command = command.split("|")
    action = command[0]
    music_piece = command[1]

    if action == "Add":
        music_composer = command[2]
        music_key = command[3]
        collection = add(music_piece, music_composer, music_key, collection)
    elif action == "Remove":
        collection = remove(music_piece, collection)
    elif action == "ChangeKey":
        new_key = command[2]
        collection = change_key(music_piece, new_key, collection)

for keys, values in collection.items():
    piece = keys
    composer = values[0]
    key = values[1]
    print(f"{piece} -> Composer: {composer}, Key: {key}")
