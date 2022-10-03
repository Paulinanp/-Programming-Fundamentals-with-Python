list_input = []

for i in range(3):
    command = input()

    list_input.append(command)

list_input[0], list_input[2] = list_input[2], list_input[0]

print(list_input)
