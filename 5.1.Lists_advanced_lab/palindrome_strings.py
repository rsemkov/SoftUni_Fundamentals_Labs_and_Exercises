words_input = input().split()
palindrome_input = input()

all_palindromes_list = [x for x in words_input if x[::] == x[::-1]]

palindrome_counter = words_input.count(palindrome_input)

print(all_palindromes_list)
print(f"Found palindrome {palindrome_counter} times")
