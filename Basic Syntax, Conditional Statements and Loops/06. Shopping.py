budget = int(input())
inputNum = input()

while inputNum != "End":
    sumNum = int(inputNum)
    budget -= sumNum

    if budget < 0:
        print("You went in overdraft!")
        break
    inputNum = input()
else:
    print("You bought everything needed.")