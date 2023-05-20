import random, time

while True:
    print ("       Game:       ")
    print (" ROCK PAPER SCISSORS")
    print (" ")
    print ("    1. ROCK")
    print ("    2. PAPER")
    print ("    3. SCISSORS")

    PersonNum= int(input("Enter your choice: "))
    
    PersonChoice= ""
    if PersonNum == 1:
        PersonChoice = "rock"
    elif PersonNum == 2:
        PersonChoice = "paper"
    elif PersonNum == 3:
        PersonChoice = "scissors"
    else :
        print("ERROR: choose a correct option")
        continue
    
        
    BotNum= random.randrange(0,3)
    Botchoice= ""
    if BotNum == 0:
        Botchoice = "rock"
    elif BotNum == 1:
        Botchoice = "paper"
    else:
        Botchoice = "scissors"
    
        
    print (" Your choice is:", PersonChoice)
    time.sleep(2)
    print (" Machine choice:", Botchoice)
    if Botchoice == PersonChoice:
        print ("¡ DRAW !")
    elif (((Botchoice == "rock" and PersonChoice == "scissors") or Botchoice == "scissors" and PersonChoice == "paper") or (Botchoice == "rock" and PersonChoice == "scissors")):
        print ("YOU LOSE.")
    elif ((Botchoice == "rock" and PersonChoice == "paper") or (Botchoice == "paper" and PersonChoice == "scissors") or (Botchoice == "scissors" and PersonChoice == "rock")):
        print ("YOU WIN")
    time.sleep(1)
    repeat= input("Want to play again? (Yes/No): ")
    if repeat.lower() != "yes":
        break
    

    


    





