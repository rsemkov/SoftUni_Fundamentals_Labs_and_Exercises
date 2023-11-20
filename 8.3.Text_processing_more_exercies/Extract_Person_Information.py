import re

lines_count = int(input())
pattern_name = r"@([A-Za-z]+)\|"
pattern_age = r"#(\d+)\*"

for _ in range(lines_count):
    line_input = input()
    name_match = re.findall(pattern_name, line_input)
    age_match = re.findall(pattern_age, line_input)
    print(f"{name_match[0]} is {age_match[0]} years old.")
