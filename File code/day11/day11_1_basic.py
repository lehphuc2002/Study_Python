import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print("!!! START !!!!\n")
check_continue = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
if(check_continue == 'n'):
    print("Ok say bye!")
player = []
computer = []
for i in range(0, 2):
    player.append(random.choice(cards))
    computer.append(random.choice(cards))
print(f"Your cards: {player}, current score: {player[0]+player[1]}")
print(f"Computer's first card: {computer[0]}")
while True:
    choose_sec = input("Type 'y' to get another card, type 'n' to pass: ")
    if choose_sec == "y":
        player.append(random.choice(cards))
        print(f"Your now cards: {player}")
        current_score = sum(player)
        print(f"Current score: {current_score}")
        if(current_score > 21):
            print("You lose because current score is higher than 21")
            break
    elif choose_sec == "n":
        current_score = sum(player)
        print(f"Current score: {current_score}")
        print(f"Computer is {computer}")
        if current_score < sum(computer):
            print(f"You lose because computer is {sum(computer)}")
            break
        elif current_score > sum(computer):
            print(f"You win because computer is {sum(computer)}")
            break
        else:
            print("Balance :))")    
            break
    else:
        break     