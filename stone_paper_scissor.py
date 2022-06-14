#stone paper seizer game
import random
list=["stone","paper","seizer"]
choice=random.choice(list)
trials=0
compfound=0
userfound=0
while(trials<10):
    userchoice=input("type anything from stone, paper or seizer")
    if userchoice=="stone" and choice=="paper":
        print("you lost!")
        compfound=compfound+1
    elif userchoice=="stone" and choice=="seizer":
        print("you won!")
        userfound=userfound+1
    elif userchoice=="paper" and choice=="stone":
        print("you won!")
        userfound = userfound + 1
    elif userchoice=="paper" and choice=="seizer":
        print("you lost!")
        compfound = compfound + 1
    elif userchoice=="seizer" and choice=="stone":
        print("you lost!")
        compfound = compfound + 1
    elif userchoice=="seizer" and choice=="paper":
        print("you won!")
        userfound = userfound + 1
    elif userchoice==choice:
        print("oops! try again")
    trials=trials+1
if compfound>userfound:
    print("game over")
elif compfound<userfound:
    print("congratulations! you won")
else:
    print("there is a tie")