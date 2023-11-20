days = int(input())
plunder_per_day = int(input())
target_plunder = int(input())

plunder_gathered = 0
for day in range(1, days + 1):
    plunder_gathered += plunder_per_day

    if day % 3 == 0:
        plunder_gathered += 0.5 * plunder_per_day

    if day % 5 == 0:
        plunder_gathered *= 0.7

if plunder_gathered >= target_plunder:
    print(f"Ahoy! {plunder_gathered:.2f} plunder gained.")
else:
    print(f"Collected only {plunder_gathered / target_plunder * 100:.2f}% of the plunder.")


