#This is the code for The classic game ROCK PAPER AND SCISSOR
print("Welcome to rock, paper and scissor.")
player=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
rock='''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
 '''
paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''
scissor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
comp=random.randint(0,2)
order=[rock,paper,scissor]

if player>=0 and player<=2:
    print("You chose:\n" +order[player])
    print("Computer chose:\n"+order[comp])
    if comp==player:
        print("Its a DRAW")
    else:
        if player==0:
            if comp==1:
                print("You Lose!")
            else:
                print("You win!")
        elif player==1:
            if comp==2:
                print("You Lose!")
            else:
                print("You win!")
        else:
            if comp==0:
                print("You Lose!")
            else:
                print("You win!")
else:
    print("You entered and invalid number, You Lose!.")
