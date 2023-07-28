import random
choice = random.randint(1,3)
print("Rock, Paper, Scissors.")
while True:
    print("A/1-Rock, B/2-Paper, C/3-Scissors.")
    userchoice = input("Enter a choice: ")
    a = 1
    b = 2
    c = 3
    print("User choice: "+str(userchoice))
    print("Ai choice: "+str(choice))
    if choice==userchoice:
        print("Tie.")
    elif userchoice==1 and choice==3 or userchoice==2 and choice==1 or userchoice==3 and choice==2:
        print("User wins.")
    else:
        print("Ai wins.")
    retry = input("Retry? y/n: ")
    if retry=="n":
        print("Thanks for playing.")
        breaks