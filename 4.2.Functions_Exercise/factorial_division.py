def factorial_calculator(num):
    num_factorial = 1
    for a in range(1, num + 1):
        num_factorial *= a
    return num_factorial


def result_generator(a, b):
    result = factorial_calculator(a) / factorial_calculator(b)
    return result


def main():
    num1 = int(input())
    num2 = int(input())
    the_result = result_generator(num1, num2)
    print(f"{the_result:.2f}")


main()

