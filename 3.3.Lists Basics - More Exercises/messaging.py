def messaging(sequence, message):
    message_elements = [_ for _ in message]

    sums_list = []
    for number in sequence:
        current_list = []
        for digit in number:
            current_list.append(int(digit))
        sums_list.append(sum(current_list))

    last_index = len(message_elements) - 1

    results_list = []
    for index in sums_list:
        if index > last_index:
            index -= last_index + 1

        results_list.append(message_elements[index])
        message_elements.pop(index)

    return results_list


sequence_input = input().split()
message_input = input()

result_to_print = messaging(sequence_input, message_input)
print("".join(result_to_print))
