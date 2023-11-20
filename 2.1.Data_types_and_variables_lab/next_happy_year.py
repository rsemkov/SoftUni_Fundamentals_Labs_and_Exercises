#we are adding 1 initially because we need the NEXT happy year, and if the initial input is a happy year, this will break it.
n = int(input()) + 1

while True:
    if len(str(n)) == len(set(str(n))):
        print(n)
        break
    n += 1

