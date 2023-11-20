budget = float(input())
price_1kg_flour = float(input())
price_1_pack_eggs = price_1kg_flour * 0.75
price_1l_milk = price_1kg_flour * 1.25
cost_per_1_loaf = price_1_pack_eggs + price_1l_milk / 4 + price_1kg_flour

number_of_loaves = 0
colored_eggs = 0
while budget >= cost_per_1_loaf:
    budget -= cost_per_1_loaf
    number_of_loaves += 1
    colored_eggs += 3
    if number_of_loaves % 3 == 0:
        colored_eggs -= number_of_loaves - 2

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")