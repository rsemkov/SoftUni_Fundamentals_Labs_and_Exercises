usernames_points = {}
submissions_counters = {}

while True:
    command = input()
    if command == "exam finished":
        break

    command = command.split("-")

    user = command[0]
    submission = command[1]

    if submission != "banned":
        points = int(command[2])

# THIS ADDS ENTRIES TO THE DIC WITH COUNTERS:
        if submission not in submissions_counters:
            submissions_counters[submission] = 0
        submissions_counters[submission] += 1

# THIS ADDS ENTRIES TO THE DIC WITH USERS AND THEIR POINTS:
        if user not in usernames_points:
            usernames_points[user] = []
        usernames_points[user].append(points)

# THIS BANS A USER:
    else:
        del usernames_points[user]

print("Results:")
for user, points in usernames_points.items():
    print(f"{user} | {max(points)}")
print("Submissions:")
for language, submissions_count in submissions_counters.items():
    print(f"{language} - {submissions_count}")
