number_sequence_input = input().split()

number_sequence_input = [int(i) for i in number_sequence_input]

result = list(filter(lambda x: x % 2 == 0, number_sequence_input))

print(result)