from tkinter import *
from tkcalendar import DateEntry
import pandas as pd
import datetime as dt

pink = "#E8A0BF"
dark_pink = "#BA90C6"
rose = "#FDF4F5"
blue = "#C0DBEA"

window = Tk()
window.title("Birthday Adder")
window.minsize(width=400, height=400)
window.config(padx=20, pady=20, bg=rose)

df = pd.read_csv("day32automatedbirthdaywisher/birthdays.csv")


def add():
    name = name_input.get()
    email = email_input.get()
    birthdate = birthdate_input.get()
    relationship = relationship_input.get()
    day, month, year = birthdate.split("/")
    age = dt.datetime.now().year - int(year)
    df.loc[len(df)] = [name, email, int(day), int(month), int(year), age, relationship]
    df.to_csv("day32automatedbirthdaywisher/birthdays.csv", index=False)
    print(df)


canvas = Canvas(width=200, height=200, bg=rose, highlightthickness=0)
image = PhotoImage(file="day32automatedbirthdaywisher/bday.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

text = Label(text="Birthday Adder", font=("Arial", 15, "bold"), bg=rose, fg=dark_pink)
text.grid(column=1, row=1)

name = Label(text="Name:", bg=rose, fg = pink, font=("Arial", 10, "bold"))
name.grid(column=0, row=2)
name.config(padx=5, pady=5)
email = Label(text="Email:", bg=rose, fg = pink, font=("Arial", 10, "bold"))
email.grid(column=0, row=3)
email.config(padx=5, pady=5)
Birthdate = Label(text="Birthdate:", bg=rose, fg = pink, font=("Arial", 10, "bold"))
Birthdate.grid(column=0, row=4)
Birthdate.config(padx=5, pady=5)
relationship = Label(text="Relationship:", bg=rose, fg = pink, font=("Arial", 10, "bold"))
relationship.grid(column=0, row=5)
relationship.config(padx=5, pady=5)

name_input = Entry(width=40)
name_input.grid(column=1, row=2, columnspan=2)
email_input = Entry(width=40)
email_input.grid(column=1, row=3, columnspan=2)
birthdate_input = DateEntry(window, width=37, bg=blue, borderwidth=2, date_pattern='dd/mm/yyyy')
birthdate_input.grid(column=1, row=4, columnspan=2)
relationship_input = Entry(width=40)
relationship_input.grid(column=1, row=5, columnspan=2)

button = Button(text="Add", bg=blue, font=("Arial", 10, "bold"), command=add)
button.grid(column=1, row=6, columnspan=2)







window.mainloop()