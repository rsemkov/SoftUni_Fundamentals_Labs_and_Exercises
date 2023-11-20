N = int(input())

for first_letter in range(97, N + 97):
    for second_letter in range(97, N + 97):
        for third_letter in range(97, N + 97):
            print(f"{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}")
