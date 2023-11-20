string_input = input().split()

for string in string_input:
    result = string * len(string)
    print(result, end="")

