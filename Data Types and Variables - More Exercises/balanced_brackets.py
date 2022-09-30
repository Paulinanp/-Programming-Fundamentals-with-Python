number_of_lines = int(input())
open_count = 0
close_count = 0

for index in range(number_of_lines):
    command = input()

    if command == "(":
        open_count += 1
    elif command == ")":
        close_count += 1
        if open_count - close_count != 0:
            print("UNBALANCED")
            exit()

if open_count == close_count:
    print("BALANCED")
else:
    print("UNBALANCED")
