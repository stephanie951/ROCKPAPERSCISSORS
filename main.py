
import random


user = ["R", "P", "S"]

#assign a random play to the computer
computer = random.choice(user)

#set player to False
player = False

while player == False:
#set player to True
    player = input("Enter a choice (R, P, S):")
    if player == computer:
        print("Player (R) : CPU (R)")
        print("Tie!")
        print(player)
    elif player == "R":
        if computer == "P":
            print("Player (R) : CPU (P)")
            print("The winner is Computer")
            break
        else:
            print("Player (R) : CPU (P)")
            print("The winner is player")
            break
    elif player == "P":
        if computer == "S":
            print("Player (P) : CPU (S)")
            print("The winner is Computer")
            break
        else:
            print("Player (P) : CPU (S)")
            print("The winner is player")
            break
    elif player == "S":
        if computer == "R":
            print("Player (S) : CPU (R)")
            print("The winner is Computer")
            break
        else:
            print("Player (S) : CPU (R)")
            print("The winner is player")
            break
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = random.choice(user)

    

        
