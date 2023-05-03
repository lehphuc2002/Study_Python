'''
travel_log = {
    "france": ["paris", "hcm", "bac_lieu"]
}
'''
clear = "\n" * 100
add_diction = {}
i = 0
winner = 0 # so tien winner dam phan thap nhat
print("Welcome to the magic trick!!!\n")
while True: 
    name = input("What is your name?: ")
    bid = input("What is your bid?: ")
    check_people = input("Are there people here? Type 'yes' or 'no': ")
    add_diction[name] = bid 
    if(check_people == "yes"):      
        print(clear)
  #      print(add_diction)
    elif(check_people == "no"):
        for a in add_diction:
            if int((add_diction[a])) > winner:
                winner = int((add_diction[a])) 
                name = a
        print(f"Nguoi chien thang la: {name} voi gia dua ra la {winner}")
        break;
                