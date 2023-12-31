#This is a colde for hangman game which is similar to BOLLYWOOD game from India
from replit import clear
#Above library is used to clear the terminal
import random
#Above library for random selection
from hangman_stages import stages,logo
from hangman_words import word_list
#To import the lists from other files
print("Welcome to the")
print(logo)
#To randomly choose a word from the list
word_to_guess=random.choice(word_list)
#To display the wword with just blanks
display=[]
for i in word_to_guess:
    display.append('_')
print(''.join(display))
lives=6
end_of_game=False   #exit statement for while loop
while not end_of_game:
    guess=input("Guess a letter: ")
    clear()     #to clear terminal everytime the user guesses
    if guess in display:    #when already guessed
        print(f"You already guessed: {guess}")
    for i in range(len(word_to_guess)):     #to replace _ with the guessed value if present
        letter = word_to_guess[i]
        if letter==guess:
            display[i]=letter
    if guess not in word_to_guess:      #if not present reduce life
        lives-=1
        if lives==0:        #loosing condition
            end_of_game=True
            print("YOU LOSE!!")
            print(f"The actual word was: {word_to_guess}")
        else:
            print(f"You guessed {guess}. It is not in the word. You loose a life.")
    print(''.join(display))     #to print the list in string form
    if '_' not in display:      #Winning condition
        end_of_game=True
        print("YOU WIN!")
    print(stages[lives])    #printing the ASCII art
