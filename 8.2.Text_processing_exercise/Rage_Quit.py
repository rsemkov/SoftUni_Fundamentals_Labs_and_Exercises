import re
pattern = r"(\D+)(\d+)"
text_input = input().upper()
matches = re.findall(pattern, text_input)

result = ""
# EACH MATCH IS A TUPLE CONTAINING THE SYMBOL AND THE NUMBER OF TIMES THIS SYMBOL SHOULD BE MULTIPLIED:
for match in matches:
    symbols_to_multiply = match[0]
    multiplier = int(match[1])
    result += symbols_to_multiply * multiplier

unique_chars = len(set(result))
print(f"Unique symbols used: {unique_chars}")
print(result)
