# numbers = input().split(" ")
# my_list = []
#
# for num in numbers:
#     my_list.append(abs(float(num)))
#
# print(my_list)

numbers = list(map(float, input().split()))
result = [abs(num) for num in numbers]
print(result)
