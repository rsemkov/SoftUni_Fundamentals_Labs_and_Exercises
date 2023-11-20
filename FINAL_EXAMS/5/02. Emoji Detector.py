import re


def multiply_list(my_list):
    # Multiply elements one by one
    result = 1
    for x in my_list:
        result = result * x
    return result


pattern_nums = r"\d"
pattern_emojis = r"([:]{2}|[*]{2})([A-Z][a-z]{2,})(\1)"
the_input = input()

matches_nums = re.findall(pattern_nums, the_input)
matches_emojis = re.findall(pattern_emojis, the_input)
matches_nums = list(map(lambda x: int(x), matches_nums))

cool_threshold = multiply_list(matches_nums)
emojis_found = len(matches_emojis)

print(f"Cool threshold: {cool_threshold}")
print(f"{emojis_found} emojis found in the text. The cool ones are:")
for match in matches_emojis:
    current_emoji = match[1]
    ascii_sum = sum(list(map(lambda x: ord(x), current_emoji)))
    if ascii_sum >= cool_threshold:
        print("".join(match))



