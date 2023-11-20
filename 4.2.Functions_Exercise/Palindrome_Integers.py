def palindrome_checker(num):
    if num == num[-1::-1]:
        return True
    else:
        return False


nums_list = input().split(", ")
for number in nums_list:
    print(palindrome_checker(number))