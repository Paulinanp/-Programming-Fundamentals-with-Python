# ornament set, 2$, 5 spirit
# tree skirt, 5$, 3 spirit
# tree garland, 3$, 10 spirit
# tree lights, 15$, 17 spirit

quantity = int(input())
days = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garland = 3
tree_lights = 15

total_spirit = 0
budget = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        total_spirit += 5
        budget += quantity * ornament_set_price

    if day % 3 == 0:
        total_spirit += 13
        budget += quantity * (tree_garland + tree_skirt_price)

    if day % 5 == 0:
        total_spirit += 17
        budget += quantity * tree_lights
        if day % 3 == 0:
            total_spirit += 30

    if day % 10 == 0:
        total_spirit -= 20
        budget += tree_lights + tree_skirt_price + tree_garland

if days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {total_spirit}")
