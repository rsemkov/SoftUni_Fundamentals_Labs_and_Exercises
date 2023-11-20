import re

pattern = r"([#|])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1"
data_input = input()
matches = re.findall(pattern, data_input)

total_cal = 0
for match, item, expiration_date, current_cal in matches:
    total_cal += int(current_cal)

print(f"You have food to last you for: {total_cal // 2000} days!")

for match, item_name, exp_date, calories in matches:
    print(f"Item: {item_name}, Best before: {exp_date}, Nutrition: {calories}")

# IN THIS SOLUTION THE WE ITERATE THROUGH THE TUPLE WITHOUT INDEXING, BY USING VARIABLES FOR EACH ITEM IN THE TUPLE #
