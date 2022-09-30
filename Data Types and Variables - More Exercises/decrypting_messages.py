key = int(input())
number_of_lines = int(input())
decrypted_message = ""

for line in range(number_of_lines):
    command = input()

    letter = ord(command) + key
    decrypted_message += chr(letter)

print(decrypted_message)

