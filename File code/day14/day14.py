import art
import random
import game_data
count = 0
countToPrint1 = 0
countToPrint2 = 0
def choice_people(people):
    name = people['name']
    description = people['description']
    country = people['country']
    followers = people['follower_count']
    if countToPrint1 == 1:
        print(f"Compare A: {name}, a {description}, from {country}")
    if countToPrint2 == 1:
        print(f"Against B: {name}, a {description}, from {country}")
    return followers
print(art.logo)
while True:
    people1 = random.choice(game_data.data)
    countToPrint1 = 1
    followers_1 = choice_people(people1)
    countToPrint1 = 0
    print(art.vs)
    people2 = random.choice(game_data.data)
    countToPrint2 = 1
    followers_2 = choice_people(people2)
    countToPrint2 = 0
    compare_followers = input("Who has more followers: Type 'A' or 'B': ")
    if compare_followers == "A":
        if int(followers_1) > int(followers_2):
            count = int(count) + 1
            print(f"You right! Current score is: {count}" )
            print("\n")
        else:
            print(f"You wrong! Current score is: {count}" )
            break
    elif compare_followers == "B":
        if int(followers_1) > int(followers_2):
            count = int(count) + 1
            print(f"You right! Current score is: {count}" )
            print("\n")
        else:
            print(f"You wrong! Current score is: {count}" )
            break
