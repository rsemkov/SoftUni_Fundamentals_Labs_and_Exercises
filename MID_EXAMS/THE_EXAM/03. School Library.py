library_books = input().split("&")


def add(name, the_list):
    if name not in the_list:
        the_list.insert(0, name)
    return the_list


def take(name, the_list):
    if name in the_list:
        the_list.remove(name)
    return the_list


def swap(first_book, second_book, the_list):
    if first_book in the_list and second_book in the_list:
        idx_1 = the_list.index(first_book)
        idx_2 = the_list.index(second_book)
        the_list[idx_1], the_list[idx_2] = the_list[idx_2], the_list[idx_1]
    return the_list


def insert(name, the_list):
    if name not in the_list:
        the_list.append(name)
    return the_list


def check(index, the_list):
    if 0 <= index < len(the_list):
        for the_index, books in enumerate(the_list):
            if the_index == index:
                print(books)
    return the_list


while True:
    command = input()
    if command == "Done":
        break
    command = command.split(" | ")
    action = command[0]

    if action == "Add Book":
        book_name = command[1]
        library_books = add(book_name, library_books)
    elif action == "Take Book":
        book_name = command[1]
        library_books = take(book_name, library_books)
    elif action == "Swap Books":
        book_1 = command[1]
        book_2 = command[2]
        library_books = swap(book_1, book_2, library_books)
    elif action == "Insert Book":
        book_name = command[1]
        library_books = insert(book_name, library_books)
    elif action == "Check Book":
        idx = int(command[1])
        library_books = check(idx, library_books)

print(", ".join(library_books))
