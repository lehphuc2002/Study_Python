print("Welcome to the tip calculator")
a = input("What was the total bill? $ ")
a = float(a)
b = input("What percentage tip would you like to give? 10, 12, or 15? ")
b = int(b)
c = input("How many people to split the bill? ")
c = int(c)
d = a * (1 + b / 100) / c
d = "{:.6f}".format(round(d, 2))
print(f"Each person should pay: ${d}")