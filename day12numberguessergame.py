import random   #for selecting random number

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\ \ | |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

def life(toughness):    #to select number of lives
    if toughness=="hard":
        return 5
    elif toughness=="easy":
        return 10
    else:
        print("Wrong toughness level try again.")
def highorlow(guessed_num,actual_num):      #to know the status of the guessed number is high low or same as actual number
    if guessed_num>actual_num:
        return "Too High\nGuess again..."
    elif guessed_num<actual_num:
        return "Too Low\nGuess again..."
    elif guessed_num==actual_num:
        return 1
def game():     #The main game code
    print("Welcome to the number guesser game!!")
    print(logo)
    print("I am thinking of a number between 1 and 100.")
    toughness=input("Choose a difficulty type 'easy' or 'hard':").lower()   #easy or hard
    lives=life(toughness)   #select lives
    actual_num=random.randint(1,100)    #randomly select number
    while(lives>0): #loop to play game
        print(f"You have {lives} attempts remaining to guess the number.")
        guessed_num=int(input("Make a guess:"))     #for guessing
        status=highorlow(guessed_num,actual_num)    #to know the status of guessed number
        if status==1:   #in case of guessed=actual
            print(f"Your guessed it right. The number was {guessed_num}.")
            break
        else:           #in case of higher or lower
            print(status)
            lives-=1
            
        if (lives==0):     #The end statement
            print(f"Game Over. The number was {actual_num}.")
game()  #calling the game function

