# The recipe is
# 1 pack eggs
# 1 kg flour
# 0.250ml milk

budget = float(input())
price_for_1kg_flout = float(input())
price_for_1pack_eggs = price_for_1kg_flout * 0.75
price_for_1l_milk = price_for_1kg_flout * 1.25
needed_milk = price_for_1l_milk / 4
count_of_colored_eggs = 0
count_of_loaf_of_bread = 0
loaf_of_bread = price_for_1kg_flout + price_for_1pack_eggs + needed_milk

while budget >= loaf_of_bread:
    budget -= loaf_of_bread
    count_of_loaf_of_bread += 1
    count_of_colored_eggs += 3

    if count_of_loaf_of_bread % 3 == 0:
        count_of_colored_eggs -= count_of_loaf_of_bread - 2

print(f"You made {count_of_loaf_of_bread} loaves of \
Easter bread! Now you have {count_of_colored_eggs} \
eggs and {budget:.2f}BGN left.")