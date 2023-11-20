# OPTION 1 - FUNCTION:
def rounder(string):
    result = [round(float(x)) for x in string]
    return result


str_input = input().split()
print(rounder(str_input))

# OPTION 2 - LIST COMPREHENSION:
# result = [round(float(x)) for x in input().split()]
# print(result)

# OPTION 3 - LAMBDA:
# str_input = input().split()
# result = list(map(lambda x: round(float(x)), str_input))
# print(result)





