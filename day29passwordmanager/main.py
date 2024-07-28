from tkinter import *
peach = "#FFE9D0"
yellow = "#FFFED3"
blue = "#BBE9FF"
purple = "#B1AFFF"

window = Tk()
window.title("Password Manager")
window.minsize(width=500, height=400)
window.config(padx=20, pady=20, bg= yellow)


def on_add():
    website = website_input.get()
    id = id_input.get()
    password = password_input.get()
    
    if len(website) == 0 or len(id) == 0 or len(password) == 0:
        print("Please fill in all fields")
    else:
        with open("day29passwordmanager/password.txt", mode="w") as data:
            data.write(f"{website} | {id} | {password}")
            website_input.delete(0, END)
            id_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()
    data.close()

canvas = Canvas(width=250, height=250, bg=yellow, highlightthickness=0)
logo = PhotoImage(file="day29passwordmanager/password.png")
canvas.create_image(125, 125, image=logo)
canvas.grid(column=1, row=0,padx=5, pady=5)

website = Label(text="Website:", bg=peach)
website.grid(column=0, row=1,padx=5, pady=5)
password = Label(text="Password:", bg=peach)
password.grid(column=0, row=3,padx=5, pady=5)
id = Label(text="Email/Username:", bg=peach)
id.grid(column=0, row=2,padx=5, pady=5)

website_input = Entry(width=60)
website_input.grid(column=1, row=1, columnspan=2)
id_input = Entry(width=60)
id_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=42)
password_input.grid(column=1, row=3)


button = Button(text="Generate Password", bg=blue)
button.grid(column=2, row=3)
add_button = Button(text="Add", width=52, command=on_add, bg = purple)
add_button.grid(column=1, row=4, columnspan=2)









window.mainloop()