def emoticon_finder(text):
    result = []
    for index, ch in enumerate(text):
        if ch == ":":
            result.append(ch + text[index + 1])
    return "\n".join(result)


print(emoticon_finder(input()))
