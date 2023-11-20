import re
data_input = input()
word = input()
pattern = rf"\b{word}\b"
matches = re.findall(pattern, data_input, re.IGNORECASE)
print(len(matches))
