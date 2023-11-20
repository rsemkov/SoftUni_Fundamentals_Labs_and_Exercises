string = input()

list = string.split(", ")
wolf_position = list.index("wolf")

if list[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {len(list) - (wolf_position + 1)}! You are about to be eaten by a wolf!")
