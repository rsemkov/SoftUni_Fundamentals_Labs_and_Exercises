def chars_range(chr1, chr2):
    chrs_between = []
    for char in range(ord(chr1) + 1, ord(chr2)):
        chrs_between.append(chr(char))
    return " ".join(chrs_between)


print(chars_range(input(), input()))