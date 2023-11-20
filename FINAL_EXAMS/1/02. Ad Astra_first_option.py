import re

pattern = r"([#|])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1"
data_input = input()
matches = re.findall(pattern, data_input)

total_cal = 0
for item in matches:
    current_cal = int(item[3])
    total_cal += current_cal

print(f"You have food to last you for: {total_cal // 2000} days!")

for match in matches:
    item_name = match[1]
    exp_date = match[2]
    calories = match[3]
    print(f"Item: {item_name}, Best before: {exp_date}, Nutrition: {calories}")

