def caesar_decipher(text):
    result_text = ""
    for ch in text:
        result_text += chr(ord(ch) + 3)
    return result_text


print(caesar_decipher(input()))

