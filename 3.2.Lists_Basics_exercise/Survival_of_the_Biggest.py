integers_list = [int(x) for x in input().split()]
count_to_remove = int(input())
for _ in range(count_to_remove):
    idx_of_smallest = integers_list.index(min(integers_list))
    integers_list.pop(idx_of_smallest)
print(*integers_list, sep=", ")
