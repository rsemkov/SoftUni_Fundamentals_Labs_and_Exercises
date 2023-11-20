sequence_input = [int(x) for x in input().split()]

average_number = sum(sequence_input) / len(sequence_input)

top_nums_list = []

for number in sequence_input:
    if number > average_number:
        top_nums_list.append(number)

top_nums_list = sorted(top_nums_list, reverse=True)

while len(top_nums_list) > 5:
    top_nums_list.pop()

if len(top_nums_list) == 0:
    print("No")
else:
    for num in top_nums_list:
        print(num, end=" ")
