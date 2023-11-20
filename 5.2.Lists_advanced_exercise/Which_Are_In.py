string_sequence_1 = input().split(", ")
string_sequence_2 = input().split(", ")

lst = []
for word1 in string_sequence_1:
    for word2 in string_sequence_2:
        if word1 in word2:

            if word1 not in lst:
                lst.append(word1)

print(lst)