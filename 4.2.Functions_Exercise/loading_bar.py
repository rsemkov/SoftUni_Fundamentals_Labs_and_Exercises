def loading_bar(number):
    if number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    else:
        percents = int(number / 10) * '%'
        dots = int((100 - number) / 10) * '.'
        return f"{number}% [{percents}{dots}]\nStill loading..."


print(loading_bar(int(input())))
