def repeating_chars_remover(text):
    current_char = ""
    result = ""
    for char in text:
        if char != current_char:
            result += char
            current_char = char
    return result


print(repeating_chars_remover(input()))
