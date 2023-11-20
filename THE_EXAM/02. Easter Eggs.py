import re
text_string = input()
pattern = r"[@#]{1,}([a-z]{3,})[@#]{1,}[^A-Za-z0-9]*/{1,}(\d+)/{1,}"
matches = re.findall(pattern, text_string)

for color, amount in matches:
    print(f"You found {amount} {color} eggs!")
