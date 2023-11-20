number_of_rooms = int(input())

number_of_room = 0
free_chairs_total = 0
all_good = True
for _ in range(number_of_rooms):
    number_of_room += 1
    chairs_visitors = input().split()

    chairs = len(chairs_visitors[0])
    visitors = int(chairs_visitors[1])
    chair_visitors_difference = abs(chairs - visitors)

    if chairs < visitors:
        print(f"{chair_visitors_difference} more chairs needed in room {number_of_room}")
        all_good = False
    else:
        free_chairs_total += chair_visitors_difference

if all_good:
    print(f"Game On, {free_chairs_total} free chairs left")
