def tribonacci_sequence(nums_count):
    results_list = [1]
    for iterations in range(nums_count - 1):
        results_list.append(sum(results_list[-1:-4:-1]))

    results_list = [str(x) for x in results_list]

    return results_list


nums_input = int(input())
print(" ".join(tribonacci_sequence(nums_input)))
