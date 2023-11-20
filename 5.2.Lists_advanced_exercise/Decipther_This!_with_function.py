def enigma(words_to_decipher):
    # contains the results of the function
    deciphered_list = []

    for word in words_to_decipher:
        # this splits the every string in the list by its elements
        element_by_element_list = [_ for _ in word]
        # two lists created, each to contain either the digits or the letters from every string in the list
        digits_list = []
        letters_list = []

        # iterating through the elements and adding them to the respective list
        for x in element_by_element_list:
            if x.isdigit():
                digits_list.append(x)
            else:
                letters_list.append(x)

        # this is the number converted to a letter, then added at the beginning of the list
        nums_to_letter = chr(int("".join(digits_list)))
        letters_list.insert(0, nums_to_letter)

        # this swaps the second and the last element of the list
        letters_list[1], letters_list[-1] = letters_list[-1], letters_list[1]

        deciphered_list.append(letters_list)

    return deciphered_list


words_input = input().split()

# printing the end result by iterating through the results list
for item in enigma(words_input):
    print("".join(item), end=" ")
