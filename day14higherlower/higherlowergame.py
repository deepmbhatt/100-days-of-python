import random   #to select from data
import os       #to clear screen
from art import logo,vs     #to import art
from data import data       #to import the data
def get_account():      #to randomly select the data
    return random.choice(data)
def details(account):   #to get the detail of the account
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return f"{name}, is a {description}, from {country}"
def check_answer(guess,a_followers,b_followers):    #to check if the guessed answer is right or not
    if a_followers>b_followers:
        return guess=="a"
    else:
        return guess=="b"
def game(): #the original game function
    score=0 #initially score is 0
    game_over=False #the end variable
    account_a=get_account() #to fetch randomly account a
    account_b=get_account() #to randomly fetch account b
    while not game_over:    #the while loop 
        print(logo)
        print(f"Score:{score}")
        account_a=account_b #exchange a and b
        account_b=get_account() 
        while account_a==account_b:     #incase of same selection of A and B
            account_b=get_account()
        print("Compare A: ", details(account_a))
        print(vs)
        print("Compare B: ", details(account_b))
        guess=input("Who has more followers? A or B: ").lower() #take the guess from user
        a_follower=account_a["follower_count"]
        b_follower=account_b["follower_count"]
        status=check_answer(guess,a_follower,b_follower)        #check the status of our guess
        os.system('cls')    #clear screen each time
        if status:      #if guess is true
            score=score+1
        else:           #if guess is false
            print(f"Game Over...\nYour final score was:{score}")
            game_over=True  #true game over as true
game()
