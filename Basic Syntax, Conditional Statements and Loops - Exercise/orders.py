number_of_oreders = int(input())
total_price = 0

for i in range(number_of_oreders):
    capsule_price = float(input())
    days = int(input())
    capsule_needed_per_day = int(input())

    if capsule_price < 0.01 or capsule_price > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsule_needed_per_day < 1 or capsule_needed_per_day > 2000:
        continue

    price = capsule_price * days * capsule_needed_per_day
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total_price:.2f}")