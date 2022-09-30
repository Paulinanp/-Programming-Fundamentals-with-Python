number_of_lines = int(input())
equal_sum = 0

for line in range(1, number_of_lines + 1):
    character = input()
    equal_sum += ord(character)

print(f"The sum equals: {equal_sum}")