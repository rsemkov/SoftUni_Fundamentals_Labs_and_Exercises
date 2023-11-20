n = int(input())

list_1= []
list_2= []
for _ in range(n):
    number = int(input())

    if number >= 0:
        list_1.append(number)
    else:
        list_2.append(number)

print(list_1)
print(list_2)
print(f"Count of positives: {len(list_1)}")
print(f"Sum of negatives: {sum(list_2)}")

