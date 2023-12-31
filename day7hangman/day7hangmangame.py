from replit import clear
import random
from hangman_stages import stages,logo
from hangman_words import word_list
print("Welcome to the")
print(logo)
word_to_guess=random.choice(word_list)
word_len=len(word_to_guess)
display=[]
lives=6
for i in word_to_guess:
    display.append('_')
print(display)
end_of_game=False
while not end_of_game:
    guess=input("Guess a letter: ")
    clear()
    if guess in display:
        print(f"You already guessed: {guess}")
    for i in range(len(word_to_guess)):
        letter = word_to_guess[i]
        if letter==guess:
            display[i]=letter
    if guess not in word_to_guess:
        print(f"You guessed {guess}. It is not in the word. You loose a life.")
        lives-=1
        if lives==0:
            end_of_game=True
            print("YOU LOSE!!")
    print(''.join(display))
    if '_' not in display:
        end_of_game=True
        print("YOU WIN!")
    print(stages[lives])
