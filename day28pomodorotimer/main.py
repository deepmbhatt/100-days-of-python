from tkinter import *
from PIL import Image, ImageTk
import time


short_break = 5
long_break = 20
work = 25
reps = 0
beige = "#FFF5E1"
coral = "#FF6969"
red = "#C80036"
navy = "#0C1844"
white = "#FFFFFF"
timer = None


window = Tk()
window.title("Pomodoro")
window.minsize(width=600, height=400)
window.config(padx=100, pady=50, bg=beige)


canvas = Canvas(width=500, height=500, bg=beige, highlightthickness=0)
doodle_img = Image.open("day28intermediatetkinter/back.png")
doodle = ImageTk.PhotoImage(doodle_img)
canvas.create_image(250, 250, image=doodle)
timer_text = canvas.create_text(250, 250, text="00:00", font=("Arial", 80, "bold"), fill=white)
canvas.grid(column=1, row=1)

def count_down(count):
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    if count == 0:
        start_timer()
        window.bell()
        mark = ""
        for _ in range(reps//2):
            mark += "✔"
        checkmarks.config(text=mark)


def start_timer():
    global reps
    work_sec = work * 60
    short_break_sec = short_break * 60
    long_break_sec = long_break * 60
    reps = reps + 1
    print(reps%2)
    if reps%2==0:
        count_down(short_break_sec)
        title_label.config(text="Short Break!!", fg=navy)
    elif reps==8:
        count_down(long_break_sec)
        title_label.config(text="Long Break!!", fg=navy)
    else:
        count_down(work_sec)
        title_label.config(text="Work!!", fg=red)

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer!!", fg=navy)



title_label = Label(text="Timer!!", font=("Calibri", 45, "bold"), fg=navy, bg=beige)
title_label.grid(column=1, row=0)

start_button = Button(text="Start", font=("Calibri", 20, "bold"), fg=white, bg=coral, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=("Calibri", 20, "bold"), fg=white,  bg=coral, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmarks = Label(text="", font=("Calibri", 20, "bold"), fg=navy, bg=beige)
checkmarks.grid(column=1, row=3)









window.mainloop()