import random

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\ \ | |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

def life(toughness):
    if toughness=="hard":
        return 5
    elif toughness=="easy":
        return 10
    else:
        print("Wrong toughness level try again.")
def highorlow(guessed_num,actual_num):
    if guessed_num>actual_num:
        return "Too High\nGuess again..."
    elif guessed_num<actual_num:
        return "Too Low\nGuess again..."
    elif guessed_num==actual_num:
        return 1
def game():
    print("Welcome to the number guesser game!!")
    print(logo)
    print("I am thinking of a number between 1 and 100.")
    toughness=input("Choose a difficulty type 'easy' or 'hard':").lower()
    lives=life(toughness)
    actual_num=random.randint(1,100)
    while(lives>0):
        print(f"You have {lives} attempts remaining to guess the number.")
        guessed_num=int(input("Make a guess:"))
        status=highorlow(guessed_num,actual_num)
        if status==1:
            print(f"Your guessed it right. The number was {guessed_num}.")
            break
        else:
            print(status)
            lives-=1
            
        if (lives==0):
            print(f"Game Over. The number was {actual_num}.")
game()

