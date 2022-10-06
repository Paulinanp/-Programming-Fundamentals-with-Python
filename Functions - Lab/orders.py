def calculate(product, quantity):
    total_sum = 0

    if product == "coffee":
        total_sum = 1.50 * quantity
    elif product == "coke":
        total_sum = 1.40 * quantity
    elif product == "water":
        total_sum = 1.00 * quantity
    elif product == "snacks":
        total_sum = 2.00 * quantity
    return total_sum


curr_product = input()
curr_quantity = int(input())
print(f"{calculate(curr_product, curr_quantity):.2f}")