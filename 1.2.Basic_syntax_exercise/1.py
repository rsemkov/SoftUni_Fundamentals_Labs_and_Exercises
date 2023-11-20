#prints out the first year that has only distinctive digits

year = int(input())

while True:
    year_in_string = str(year)
    year_in_set = set(year_in_string)

    if len(year_in_string) == len(year_in_set):
        print(year)
        break

    year += 1
