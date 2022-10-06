def grade(number):
    result = ""

    if 2.00 <= number <= 2.99:
        result = "Fail"
    elif 3.00 <= number <= 3.49:
        result = "Poor"
    elif 3.50 <= number <= 4.49:
        result = "Good"
    elif 4.50 <= number <= 5.49:
        result = "Very Good"
    elif 5.50 <= number <= 6.00:
        result = "Excellent"

    return result


curr_num = float(input())
print(grade(curr_num))