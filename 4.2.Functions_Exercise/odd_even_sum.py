def odd_even_sum(nums_string):
    even_digits = [int(x) for x in nums_string if int(x) % 2 == 0]
    odd_digits = [int(y) for y in nums_string if int(y) % 2 != 0]
    sum_of_odd_digits = sum(odd_digits)
    sum_of_even_digits = sum(even_digits)

    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"


print(odd_even_sum(input()))




