# string = input()
# num = int(input())
#
# result = lambda a, b: a * b
#
# print(result(string, num))

def repeat(string, num):
    repeated_str = string * num
    return repeated_str


curr_str = input()
curr_num = int(input())
print(repeat(curr_str, curr_num))