word = input()

reversed_word = ""

for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]

print(reversed_word)

#second way to reverse a word in python with slice method
#word = input()
#
#print(word[::-1])