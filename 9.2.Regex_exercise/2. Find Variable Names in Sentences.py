import re
pattern = r"\b_([A-Za-z0-9]+)\b"
data_input = input()
matches = re.findall(pattern, data_input)

print(",".join(matches))


