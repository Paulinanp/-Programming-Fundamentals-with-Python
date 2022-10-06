money_receive = input().split(", ")
count_of_beggars = int(input())

money_receive_digit = []
for element in money_receive:
    money_receive_digit.append(int(element))

final_sum = []
starting_index = 0

while starting_index < count_of_beggars:
    sum_for_curr_beggar = 0

    for index in range(starting_index, len(money_receive_digit), count_of_beggars):
        sum_for_curr_beggar += money_receive_digit[index]

    final_sum.append(sum_for_curr_beggar)
    starting_index += 1

print(final_sum)