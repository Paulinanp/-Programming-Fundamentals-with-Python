number_of_lines = int(input())
tank_capacity = 255
litters_of_water = 0

for line in range(number_of_lines):
    litters = int(input())

    if tank_capacity - litters < 0:
        print("Insufficient capacity!")
        continue

    tank_capacity -= litters
    litters_of_water += litters

print(litters_of_water)








