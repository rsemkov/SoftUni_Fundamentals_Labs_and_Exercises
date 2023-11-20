happiness_list = input().split()
factor = int(input())

multiplied_list = list(map(lambda x: int(x) * factor, happiness_list))

average_happiness = sum(multiplied_list) / len(multiplied_list)

filtered_list = list(filter(lambda y: y >= average_happiness, multiplied_list))

happy_count = len(filtered_list)
total_count = len(happiness_list)

if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
