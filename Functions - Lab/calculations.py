def calculation(operation, num1, num2):
    result = 0
    if operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = int(num1 / num2)
    elif operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    return result


curr_operation = input()
curr_num1 = int(input())
curr_num2 = int(input())

print(calculation(curr_operation, curr_num1, curr_num2))