allowed_events_list = ["coding", "cat", "dog", "movie"]
coffees_needed = 0

while True:
    command = input()
    if command == "END":
        break

    if command.lower() not in allowed_events_list:
        continue

    if command.islower():
        coffees_needed += 1
    else:
        coffees_needed += 2

if coffees_needed > 5:
    print("You need extra sleep")
else:
    print(coffees_needed)
