from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=20)
window.config(padx=20, pady=20)

text1 = Label(text="is equal to")
text2 = Label(text="Miles")
text3 = Label(text="Km")
text4 = Label(text="0")
text1.grid(column=0, row=1)
text2.grid(column=2, row=0)
text3.grid(column=2, row=1)
text4.grid(column=1, row=1)

input = Entry(width=10)
input.grid(column=1, row=0)

def button_clicked():
    text4["text"] = float(input.get()) * 1.60934

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)






window.mainloop()
