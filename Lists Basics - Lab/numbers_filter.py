number_of_lines = int(input())
list_of_numbers = []

COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_NEGATIVE = "negative"
COMMAND_POSITIVE = "positive"

for i in range(number_of_lines):
    number = int(input())
    list_of_numbers.append(number)

command = input()
filtred_numbs = []

for n in list_of_numbers:
    filtred = (
        (command == COMMAND_EVEN and n % 2 == 0) or
        (command == COMMAND_ODD and n % 2 != 0) or
        (command == COMMAND_POSITIVE and n >= 0) or
        (command == COMMAND_NEGATIVE and n < 0)
    )

    if filtred:
        filtred_numbs.append(n)

print(filtred_numbs)