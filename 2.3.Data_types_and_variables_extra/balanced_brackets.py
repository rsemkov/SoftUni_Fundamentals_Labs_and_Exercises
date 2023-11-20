n = int(input())

string = ""
brackets_only_string = ""

for _ in range(n):
    symbol = input()
    string += symbol

for item in string:
    if item == "(" or item == ")":
        brackets_only_string += item

while '()' in brackets_only_string:
    brackets_only_string = brackets_only_string.replace('()','*')

if all(_ == '*' for _ in brackets_only_string):
    print("BALANCED")
else:
    print("UNBALANCED")









