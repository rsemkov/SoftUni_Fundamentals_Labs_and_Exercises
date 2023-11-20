banned_words = input().split(", ")
text_input = input()

for word in banned_words:
    text_input = text_input.replace(word, "*" * len(word))

print(text_input)
