start_char = int(input())
end_char = int(input())
result = ""

for char in range(start_char, end_char + 1):
    result += chr(char) + " "

print(result)