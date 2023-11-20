def group_sorter(nums):
    limit = int(nums[-1]) // 10 if int(nums[-1]) % 10 == 0 else int(nums[-1]) // 10 + 1
    results_list = []

    for group in range(1, limit + 1):
        current_list = []
        for number in nums:
            if (group - 1) * 10 < int(number) <= group * 10:
                current_list.append(int(number))

        results_list.append(f"Group of {group * 10}'s: {current_list}")

    return results_list


numbers_input = input().split(", ")

for item in group_sorter(numbers_input):
    print(item)

