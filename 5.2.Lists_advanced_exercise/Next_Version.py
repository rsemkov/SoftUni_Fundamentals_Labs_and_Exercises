def version_changer(version):
    current_version = int(version[0] + version[2] + version[4])
    next_version = str((current_version + 1))
    next_version_list = [item for item in next_version]
    return next_version_list


version_str_input = input()
print(".".join(version_changer(version_str_input)))

