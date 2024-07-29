from tkinter import *
from tkinter import messagebox
import pyperclip
import json
peach = "#FFE9D0"
yellow = "#FFFED3"
blue = "#BBE9FF"
purple = "#B1AFFF"

window = Tk()
window.title("Password Manager")
window.minsize(width=500, height=400)
window.config(padx=20, pady=20, bg= yellow)

def on_search():
    website = website_input.get()
    email = id_input.get()
    print(email)
    try:
        with open("day30enhancedpasswordmanager/password.json", mode="r") as data:
            dict = json.load(data)
            try:
                status.config(text = "Password found", bg=peach)
                if website in dict:
                    email = dict[website]["email"]
                    password = dict[website]["password"]
                    messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
                else:
                    messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
            except KeyError:
                status.config(text = "Password not found", bg=peach)


    except FileNotFoundError:
        status.config(text = "File not found", bg=peach)
    
    except json.decoder.JSONDecodeError:
        status.config(text = "File is empty", bg=peach)

    finally:
        data.close()
    


def on_add():

    website = website_input.get()
    email = id_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        status.config(text="Please make sure you haven't left any fields empty.", bg=peach)
    else:
        try:
            with open("day30enhancedpasswordmanager/password.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("day30enhancedpasswordmanager/password.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("day30enhancedpasswordmanager/password.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            id_input.delete(0, END)
            password_input.delete(0, END)
            status.config(text = "Password saved", bg=peach)
            website_input.focus()

def on_generate():
    #This is a code to generate a password as per required number of letters, symbols and numbers
    import random
    n_let= 8
    n_sym= 2
    n_num= 2
    n_cap= 2
    letters=[]
    numbers=[]
    symbols=[]
    capital=[] 
    for i in range(65,91):
        capital.append(chr(i))
    for i in range(98,123):
        letters.append(chr(i))
    numbers=['0','1','2','3','4','5','6','7','8','9']
    symbols=['!','@','#','$','%','&','*','(',')','+']
    password=[]
    for i in range(n_let):
        password+=random.choice(letters)
    for i in range(n_cap):
        password+=random.choice(capital)
    for i in range(n_sym):
        password+=random.choice(symbols)
    for i in range(n_num):
        password+=random.choice(numbers)
    password=''.join(random.sample(password,len(password)))
    password_input.insert(0,password)
    pyperclip.copy(password)


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

website_input = Entry(width=42)
website_input.grid(column=1, row=1)
search_button = Button(text="Search", bg=blue, command=on_search)
search_button.grid(column=2, row=1)
id_input = Entry(width=60)
id_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=42)
password_input.grid(column=1, row=3)


button = Button(text="Generate Password", bg=blue, command=on_generate)
button.grid(column=2, row=3)
add_button = Button(text="Add", width=52, command=on_add, bg = purple)
add_button.grid(column=1, row=4, columnspan=2)

status = Label(text="Enter Values...", bg=peach)
status.grid(column=1, row=5, columnspan=2)

window.mainloop()