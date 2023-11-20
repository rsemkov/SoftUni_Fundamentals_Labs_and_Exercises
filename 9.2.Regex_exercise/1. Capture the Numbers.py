import re
while True:
    str_input = input()
    if str_input == "":
        break
    pattern = r"\d+"
    matches = re.findall(pattern, str_input)
    for match in matches:
        print(match, end=" ")
