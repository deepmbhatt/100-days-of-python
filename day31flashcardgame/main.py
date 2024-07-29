BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random

window = Tk()
window.title("Flashy")
window.minsize(width=900, height=600)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

try:
    data = pd.read_csv("day31flashcardgame/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("day31flashcardgame/data/hindi-words.csv")
    #print(original_data)
    words = original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    print(current_card)
    canvas.itemconfig(card_title, text="Hindi", fill="black")
    canvas.itemconfig(card_word, text=current_card["Hindi"], fill="black")
    canvas.itemconfig(card_front, image=card_front)
    flip_timer = window.after(3000, func=flip_card)
    
def is_known():
    words.remove(current_card)
    next_card()
    data = pd.DataFrame(words)
    data.to_csv("day31flashcardgame/data/words_to_learn.csv", index=False)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


current_card = {}
flip_timer = window.after(3000, func=flip_card)




canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="day31flashcardgame/images/card_front.png")
card_back_img = PhotoImage(file="day31flashcardgame/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

unknown_image = PhotoImage(file="day31flashcardgame/images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

known_image = PhotoImage(file="day31flashcardgame/images/right.png")
known_button = Button(image=known_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)


next_card()


window.mainloop()
