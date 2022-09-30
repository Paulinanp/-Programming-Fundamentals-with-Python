number_of_snowballs = int(input())
max_weight = 0
max_time = 0
max_quality = 0
max_value = 0

for snowball in range(number_of_snowballs):
    weight_of_the_snowball = int(input())
    time_needed = int(input())
    quality = int(input())
    value = (weight_of_the_snowball / time_needed) ** quality

    if value > max_value:
        max_weight = weight_of_the_snowball
        max_time = time_needed
        max_quality = quality
        max_value = value

print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")
