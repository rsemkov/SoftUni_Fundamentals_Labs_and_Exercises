phonebook = {}
contacts_search_list = []
while True:
    new_contact = input()
    if new_contact.isdigit():
        break

    new_contact = new_contact.split("-")
    name = new_contact[0]
    phone = new_contact[1]
    phonebook[name] = phone

for _ in range(int(new_contact)):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")