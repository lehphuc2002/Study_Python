import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
chuoixamloz1 = ""
chuoixamloz2 = ""
chuoixamloz3 = ""
for i in range(0,nr_letters):
    ngaunhien1 = random.choice(letters)
    chuoixamloz1 = chuoixamloz1 + ngaunhien1
for i in range(0,nr_symbols):
    ngaunhien2 = random.choice(symbols)
    chuoixamloz2 = chuoixamloz2 + ngaunhien2
for i in range(0,nr_numbers):
    ngaunhien3 = random.choice(numbers)
    chuoixamloz3 = chuoixamloz3 + ngaunhien3
chuoifull = chuoixamloz1 + chuoixamloz2 + chuoixamloz3
print(f"Day la chuoi theo thu tu: {chuoifull}")
chuoifull_EoTheoThuTu = ""
for i in range(0,len(chuoifull)):
    ngaunhienfull = random.choice(chuoifull)
    vitricua_ngaunhienfull = chuoifull.find(ngaunhienfull)
    chuoifull = chuoifull[:vitricua_ngaunhienfull] + chuoifull[vitricua_ngaunhienfull+1:]
    chuoifull_EoTheoThuTu = chuoifull_EoTheoThuTu + ngaunhienfull
print(f"Day la chuoi eo theo thu tu: {chuoifull_EoTheoThuTu}")