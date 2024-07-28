import tkinter

window = tkinter.Tk()
window.title("Button click")
window.minsize(width=500, height=300)

def button_clicked():
    my_label["text"] = "Button clicked"

button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

input = tkinter.Entry(width=10)
input.pack()

def other_clicked():
    my_label["text"] = input.get()

other_button = tkinter.Button(text="Click me", command=other_clicked)
other_button.pack()



window.mainloop()