price_without_tax = 0
special_customer = False

while True:
    command = input()

    if command == "special":
        special_customer = True
        break
    if command == "regular":
        break

    command = float(command)

    if command <= 0:
        print("Invalid price!")
        continue

    price_without_tax += command

taxes = price_without_tax * 0.2
price_with_tax = price_without_tax + taxes

if special_customer:
    price_with_tax *= 0.9

if price_with_tax == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_tax:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {price_with_tax:.2f}$")
