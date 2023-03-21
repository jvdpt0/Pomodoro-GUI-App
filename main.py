from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text= 'Timer')
    canvas.itemconfig(current_timer, text='00:00')
    checkmark_label.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN *60
    long_break = LONG_BREAK_MIN *60

    if reps % 8 == 0:
        timer_label.config(text= 'Break', fg = RED)
        countdown(long_break)
    elif reps % 2 == 0:
        timer_label.config(text= 'Break', fg = PINK)
        countdown(short_break)
    else:
        timer_label.config(text= 'Work', fg = GREEN)
        countdown(work_time)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(current_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        checks = ''
        work_reps = math.floor(reps/2)
        for n in range(work_reps):
            checks += '✔'
        checkmark_label.config(text=checks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg = YELLOW)

canvas = Canvas(width=200, height=224, bg = YELLOW, highlightthickness=0)
img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=img)
current_timer = canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column = 1 ,row = 1)

timer_label = Label(text= 'Timer', font=(FONT_NAME,50), fg = GREEN, bg = YELLOW)
timer_label.grid(column = 1, row = 0)

checkmark_label = Label(fg= GREEN, bg = YELLOW)
checkmark_label.grid(column = 1, row = 3)

start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()