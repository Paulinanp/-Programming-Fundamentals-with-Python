number = int(input())
message = ""

for i in range(number):
    string_input = input()

    if '_' in string_input:
        message = "is not pure!"
    elif ',' in string_input:
        message = "is not pure!"
    elif '.' in string_input:
        message = "is not pure!"
    else:
        message = "is pure."

    print(f"{string_input} {message}")
