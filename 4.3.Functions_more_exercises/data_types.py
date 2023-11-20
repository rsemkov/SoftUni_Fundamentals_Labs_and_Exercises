def data_handler(data_type, data):
    result = None
    if data_type == "int":
        result = int(data) * 2
    elif data_type == "real":
        result = f"{float(data) * 1.5:.2f}"
    elif data_type == "string":
        result = "$" + data + "$"

    return result


data_type_input = input()
the_input = input()

print(data_handler(data_type_input, the_input))