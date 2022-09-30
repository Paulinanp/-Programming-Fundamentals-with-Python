num_line = int(input())

for i in range(num_line):
    curr_num = int(input())

    if not curr_num % 2 == 0:
        print(f"{curr_num} is odd!")
        break
else:
    print("All numbers are even.")