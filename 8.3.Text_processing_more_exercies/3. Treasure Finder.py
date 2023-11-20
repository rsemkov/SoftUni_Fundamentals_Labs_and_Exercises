import re
keys = [int(x) for x in input().split()]
treasure_pattern = r"&(.+)&"
coordinates_pattern = r"<(.+)>"

while True:
    str_input = input()
    if str_input == "find":
        break

    result = ""
    index = 0
    for item in str_input:
        # THIS RESETS THE INDEX TO THE FIRST INDEX IF IT REACHES THE END OF THE KEYS SEQUENCE
        if index == len(keys):
            index = 0
        result += chr(ord(item) - keys[index])
        index += 1
    # THE REGEX FINDS THE TREASURE AND ITS COORDINATES
    treasure_match = re.findall(treasure_pattern, result)
    coordinates_match = re.findall(coordinates_pattern, result)
    print(f"Found {treasure_match[0]} at {coordinates_match[0]}")
