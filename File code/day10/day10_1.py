def addCalculate(a, b):
    return a + b


def subCalculate(a, b):
    return a - b


def mulCalculate(a, b):
    return a * b


def divCalculate(a, b):
    return a / b


choose = {"+": addCalculate, "-": subCalculate, "*": mulCalculate, "/": divCalculate}
num1 = int(input("Choose num1: "))
num2 = int(input("Choose num2: "))
choice = input("Choose your choice (+ - * /): ")

if choose[choice] == addCalculate:
    a = addCalculate(num1, num2)
    print(f"{a}")
elif choose[choice] == subCalculate:
    a = subCalculate(num1, num2)
    print(f"{a}")
elif choose[choice] == mulCalculate:
    a = mulCalculate(num1, num2)
    print(f"{a}")
elif choose[choice] == divCalculate:
    a = divCalculate(num1, num2)
    print(f"{a}")
else:
    print("Wrong choice")
