import re
pattern = r"([@#])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
data_input = input()
matches = re.findall(pattern, data_input)

results = {}
matches_count = 0
for match in matches:
    matches_count += 1
    first_word = match[1]
    second_word = match[2]
    if first_word == second_word[-1::-1]:
        results[first_word] = second_word

if matches_count == 0:
    print("No word pairs found!")
else:
    print(f"{matches_count} word pairs found!")

if len(results) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    mirror_word_pairs = [f"{word_one} <=> {word_two}" for word_one, word_two in results.items()]
    print(", ".join(mirror_word_pairs))
