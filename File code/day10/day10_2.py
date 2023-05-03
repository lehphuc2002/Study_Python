def addCalculate(a, b):
    return a + b

def subCalculate(a, b):
    return a - b

def mulCalculate(a, b):
    return a * b

def divCalculate(a, b):
    return a / b

choose = {"+": addCalculate, "-": subCalculate, "*": mulCalculate, "/": divCalculate}
num1 = float(input("Choose num1: "))
num2 = float(input("Choose num2: "))
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
checkContinue = input(f"Want continue? type y for calculated with {a}, type n for exit: ")
real_next = a
while checkContinue == "y":
    next_num = input("Next number is: ")
    choice = input("Choose your next choice (+ - * /): ")
    calculate_now = choose[choice]
    num1 = float(next_num)
    print("num1: ", num1)
    a = float(real_next)
    print("a: ", a)
    real_next = calculate_now(float(a), float(num1))
    print("Gia tri sau la: ", real_next)
    checkContinue = input(f"Want continue? type y for calculated with {real_next}, type n for exit: ")
    if checkContinue == "no":
        break
