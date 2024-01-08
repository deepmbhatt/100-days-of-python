#to print the black jack logo
from logo import logo
#to select from random cards
import random
#to clear screen
import os
#to select the cards on random
def sel_cards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
#to calculate the score of user and computer cards
def score(cards):
    if sum(cards)==21 and len(cards)==2:        #returns 0 means 21 reached already
        return 0
    if sum(cards)>21 and 11 in cards:       #in case of 11 and going above 21
        cards.append(1)
        cards.remove(11)
    return sum(cards)
def compare(user_score,computer_score):     #to compare the scores
    if user_score>21 and computer_score>21:
        return "You went over. YOU LOSE!! 🙁"
    if user_score==computer_score:
        return "It's a DRAW!! 😪"
    elif user_score==0:
        return "You WIN!!!! 🎇🧨🤑"
    elif user_score>21:
        return "You went over. YOU LOSE!! 🙁"
    elif computer_score>21:
        return "Opponent went over. You WIN!!!! 🎇🧨🤑"
    elif user_score>computer_score:
        return "You WIN!!!! 🎇🧨🤑"
    else:
        return "YOU LOSE!! 🙁"
def game():     #main game function
    print(logo)
    user_cards=[]
    computer_cards=[]
    game_over=False     #condition for while loop
    for i in range(2):  #to initially select two cards
        user_cards.append(sel_cards())
        computer_cards.append(sel_cards())
    while not game_over:    #the second half calculation
        user_score=score(user_cards)
        computer_score=score(computer_cards)
        print(f"Your cards are: {user_cards} and the total score is: {user_score}")
        print(f"Computer's first card is: {computer_cards[0]}")
        if user_score==0 or computer_score==0 or user_score>21:     #incase of getting 21 or higher
            game_over=True
        else:   #to select a new card
            user_deal=input("Type 'y' to get another card and type 'n' to pass: ")
            if user_deal=="y":
                user_cards.append(sel_cards())
            else:
                game_over=True
    while computer_score!=0 and computer_score<17:  #further programming for computer
        computer_cards.append(sel_cards())
        computer_score=score(computer_cards)
    print(f"Your final hand: {user_cards} and the final score is: {user_score}")
    print(f"Computer's final hand: {computer_cards} and the final score is: {computer_score}")
    print(compare(user_score,computer_score))
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")=="y":     #to play game yes or no
    os.system('cls')
    game()
