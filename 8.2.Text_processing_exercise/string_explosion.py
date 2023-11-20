text_input = input()
skip_counter = 0
result = ""
for index, ch in enumerate(text_input):
    if ch == ">":
        result += ch
    elif ch.isdigit():
        skip_counter += int(ch) - 1
    else:
        if skip_counter == 0:
            result += ch
        else:
            skip_counter -= 1

print(result)
