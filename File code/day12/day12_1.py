""""
enemies = 1
def inc_enemise():
    print(f"before: {enemies}")
    return enemies+1
enemies = inc_enemise()
print(f"after: {enemies}")
"""
import random
ran_num = 0
def select_mode(mode):
    if(mode == "hard"):
        print("You have 5 times to guess")
        return so_mang + 5
    elif(mode == "easy"):
        print("You have 10 times to guess")
        return so_mang + 10
def guess_number():
    num_guess = int(input("Guess number: "))
    if(num_guess == ran_num):
        print("You win")
        return 1
    elif(num_guess > ran_num):
        print("The real number is less than you guessed")
        return 0
    elif(num_guess < ran_num):
        print("The real number is higher than you guessed")
        return 0
while True:
    so_mang = 0
    print("Welcome!!!")
    print("I'm thinking about random number between 1 and 100")
    ran_num = random.randint(1,100)
    print(f"Shhhh, this is {ran_num}, don't tell anyone")
    mode_choose = input("Choose mode: 'easy' or 'hard': ")
    so_mang = select_mode(mode_choose)
    while True:
        check_break = guess_number()
        if check_break == 0:
            so_mang = so_mang - 1
            if so_mang == 0:
                print("You lose")
                break
        if check_break == 1:
                break    
    out_game = input("Want to play more: 'yes' or 'no': ")        
    if out_game == "no":
            break