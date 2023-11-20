import re
pattern = r"^[A-Za-z0-9_-]{3,16}$"
text_input = input().split(", ")

for word in text_input:
    if re.match(pattern, word):
        print(word)
