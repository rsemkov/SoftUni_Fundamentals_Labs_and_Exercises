def pass_validator(password):
    results_list = []
    digits_counter = 0
    letters_digits = True

    if len(password) < 6 or len(password) > 10:
        results_list.append("Password must be between 6 and 10 characters")

    for char in password:
        if not char.isalnum():
            letters_digits = False
            break
    if not letters_digits:
        results_list.append("Password must consist only of letters and digits")

    for char in password:
        if char.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        results_list.append("Password must have at least 2 digits")

    return results_list


result = pass_validator(input())
if len(result) == 0:
    print("Password is valid")
else:
    for item in result:
        print(item)

