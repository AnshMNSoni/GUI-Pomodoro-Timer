# Day :: 28
from tkinter import *
import math

# Constants:
PINK = '#e2979c'
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f7f5dd'
FONT_NAME = 'Courier'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# Timer Reset:
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= '00:00')
    title_label.config(text='Timer') 
    chechmark.config(text='')
    global reps
    reps = 0
    
# Timer Mechanism:
def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text='Break', fg=RED)
        
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text='Break', fg=PINK)
        
    else:
        count_down(work_sec)
        title_label.config(text='WORK', fg=GREEN)
    
# Countdown Mechanism:
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if (count_sec < 10):
        count_sec = f'0{count_sec}'
    
    if (count_min < 10):
        count_min = f'0{count_min}'
        
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if (count>0):
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += '✔️'
        chechmark.config(text=marks)
            
# UI setup:
window = Tk()
window.title('Pomodoro')
window.config(padx=150, pady=70, bg=YELLOW)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 28, 'bold'))
canvas.grid(column=1, row=1)

title_label = Label(text='Timer', font=(FONT_NAME, 40, 'bold'), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

start = Button(text='Start', font=(FONT_NAME, 12, 'bold'), highlightthickness=0, bg=YELLOW, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text='Reset', font=(FONT_NAME, 12, 'bold'), highlightthickness=0, bg=YELLOW, command=reset_timer)
reset.grid(column=2, row=2)

chechmark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, 'bold'))
chechmark.grid(column=1, row=3)

window.mainloop()