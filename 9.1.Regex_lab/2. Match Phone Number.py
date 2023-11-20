import re
numbers = input()
regex = r"(\+359)([\s-])(2)(\2)(\d{3})(\2)(\d{4})\b"

matches = re.findall(regex, numbers)

formatted_matches = ["".join(match) for match in matches]

print(", ".join(formatted_matches))
