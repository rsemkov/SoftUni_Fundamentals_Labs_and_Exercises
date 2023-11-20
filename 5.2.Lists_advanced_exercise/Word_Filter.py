some_text = input().split()

even_len_list = list(filter(lambda x: len(x) % 2 == 0, some_text))

for item in even_len_list:
    print(item)
