# fruits = [
#     "Strawberries",
#     "Nectarines",
#     "Apples",
#     "Grapes",
#     "Peaches",
#     "Cherries",
#     "Pears",
# ]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[0])
# print(dirty_dozen[1])
# print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])
bua = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

bao = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

keo = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
listKeoBuaBao = [keo, bua, bao]
a = input("May chon cai nao? 1 la keo, 2 la bua, 3 la bao, chon di: ")
a = int(a)
print(f"may da chon {a} la {listKeoBuaBao[a-1]} ");
PC_chon = random.randint(0,2);
PC_chon = int(PC_chon)   #ko tac dung
print(f"PC da chon {PC_chon+1} la {listKeoBuaBao[PC_chon]} ")
if a == (PC_chon + 1):
    print("Hue roi nha")
elif a == 1 and (PC_chon + 1 == 2):
    print("Thua PC roi") 
elif a == 1 and (PC_chon + 1 == 3):
    print("Thang PC roi")
elif a == 2 and (PC_chon + 1 == 1):
    print("Thang PC roi")
elif a == 2 and (PC_chon + 1 == 3):
    print("Thua PC roi")
elif a == 3 and (PC_chon + 1 == 1):
    print("Thua PC roi")
else:
    print("Thang PC roi")