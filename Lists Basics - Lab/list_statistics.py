numbers_of_line = int(input())
posetive_numbers_list = []
negative_numbers_list = []

for i in range(numbers_of_line):
    number = int(input())

    if number < 0:
        negative_numbers_list.append(number)
    else:
        posetive_numbers_list.append(number)

print(posetive_numbers_list)
print(negative_numbers_list)
print(f"Count of positives: {len(posetive_numbers_list)}")
print(f"Sum of negatives: {sum(negative_numbers_list)}")