n = int(input())

sum_chars = 0
for _ in range(n):
    char = input()

    sum_chars += ord(char)

print(f"The sum equals: {sum_chars}")