file_path = input().split("\\")

file_name, file_extension = file_path[-1].split(".")

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")


# REGEX SOLUTION ALTERNATIVE:

# import re
# pattern = r"\\([^\\.]+)\.([^\\.]+)$"
# file_name = input()
# matches = re.findall(pattern, file_name)
# for match in matches:
#     print(f"File name: {match[0]}\nFile extension: {match[1]}")

