import sys
n = int(input())

best_ball = -sys.maxsize
best_weight = 0
best_time = 0
best_quality = 0

for _ in range(n):
    ball_weight = int(input())
    ball_speed = int(input())
    ball_quality = int(input())

    current_ball_value = (ball_weight / ball_speed) ** ball_quality

    if current_ball_value > best_ball:
        best_ball = current_ball_value
        best_weight = ball_weight
        best_time = ball_speed
        best_quality = ball_quality

print(f"{best_weight} : {best_time} = {int(best_ball)} ({best_quality})")

