n = int(input())
CAPACITY = 255
water_in_tank = 0

for _ in range(n):
    water_litres = int(input())
    if water_in_tank + water_litres > CAPACITY:
        print("Insufficient capacity!")
        continue
    water_in_tank += water_litres

print(water_in_tank)
