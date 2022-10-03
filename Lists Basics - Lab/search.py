number_of_lines = int(input())
word = input()
list_of_word = []

for line in range(number_of_lines):
    curr_sense = input()
    list_of_word.append(curr_sense)

print(list_of_word)

for i in range(len(list_of_word) - 1, -1, -1):
    element = list_of_word[i]
    if word not in element:
        list_of_word.remove(element)
print(list_of_word)



