def positive(nums):
    return [a for a in numbers_input if int(a) >= 0]


def negative(nums):
    return [b for b in numbers_input if int(b) < 0]


def even(nums):
    return [c for c in numbers_input if int(c) % 2 == 0]


def odd(nums):
    return [d for d in numbers_input if int(d) % 2 != 0]


numbers_input = input().split(", ")
print("Positive:", ", ".join(positive(numbers_input)))
print("Negative:", ", ".join(negative(numbers_input)))
print("Even:", ", ".join(even(numbers_input)))
print("Odd:", ", ".join(odd(numbers_input)))
