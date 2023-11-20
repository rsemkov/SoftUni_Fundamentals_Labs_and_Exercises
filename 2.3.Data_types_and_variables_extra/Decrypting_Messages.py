key = int(input())
n = int(input())

decrypted_word = ""
for _ in range(n):
    letter = input()

    added_letter = ord(letter) + key
    added_letter = chr(added_letter)

    decrypted_word += added_letter

print(decrypted_word)



