from tkinter import *

window = Tk()
window.title("Widgets")
window.minsize(width=500, height=300)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

button = Button(text="Click me")
button.pack()

input = Entry(width=10)
input.pack()

text_box = Text(height=5, width=30, font=("Arial", 12, "bold"))
text_box.focus()
text_box.insert(END, "This is a text box")
text_box.pack()

scroll = Scrollbar()
scroll.pack(side=RIGHT, fill=Y)

slide = Scale(from_=0, to=100)
slide.pack()

radio = Radiobutton(text="Radio button", variable=1)
radio.pack()
radioa = Radiobutton(text="Radio button", variable=1)
radioa.pack()

check = Checkbutton(text="A")
check.pack()

checka = Checkbutton(text="B")
checka.pack()

spin = Spinbox(from_=0, to=10)
spin.pack()

list_box = Listbox(height=3)
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    list_box.insert(END, fruit)

list_box.pack()


window.mainloop()