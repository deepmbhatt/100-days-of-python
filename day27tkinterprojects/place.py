from tkinter import *

window = Tk()
window.title("Application")
window.minsize(width=500, height=300)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.place(x=100, y=100)

input = Entry(width=10)
input.place(x=100, y=150)

def button_clicked():
    my_label["text"] = input.get()

button = Button(text="Click me", command=button_clicked)
button.place(x=100, y=200)





window.mainloop()
