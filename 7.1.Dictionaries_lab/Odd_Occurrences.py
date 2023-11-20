words_input = [x.lower() for x in input().split()]
odd_occurrence_words = []

for word in words_input:
    if (word not in odd_occurrence_words) and (words_input.count(word) % 2 != 0):
        odd_occurrence_words.append(word)

for item in odd_occurrence_words:
    print(item, end=" ")

