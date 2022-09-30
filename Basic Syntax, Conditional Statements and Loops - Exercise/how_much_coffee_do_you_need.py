text = input()
coffee_count = 0
activities = ["coding", "dog", "cat", "movie"]
activities_upper = [x.upper() for x in activities]

while text != "END":
    if text == text.lower():
        if text in activities:
            coffee_count += 1
    else:
        if text in activities_upper:
            coffee_count += 2

    text = input()

if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)

