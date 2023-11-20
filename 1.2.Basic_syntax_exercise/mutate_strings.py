string_one = [_ for _ in input()]
string_two = [_ for _ in input()]

for index in range(len(string_one)):
    if string_one[index] != string_two[index]:
        string_one[index] = string_two[index]
        print("".join(string_one))
