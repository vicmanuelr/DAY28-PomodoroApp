from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
# Window related
window = Tk()
window.title("Pomodoro")
window.config(padx=25, pady=50, bg=YELLOW)

# Labels
title = Label(text="Timer", font=(FONT_NAME, 35), bg=YELLOW, fg=GREEN, justify="center")
check_mark = Label(text="✔", font=(FONT_NAME, 35), bg=YELLOW, fg=GREEN, justify="center")
title.grid(column=1, row=0)
check_mark.grid(column=1, row=3)

# Buttons
start = Button(text="Start", bg=GREEN, font=FONT_NAME, activebackground=GREEN, highlightthickness=0)
reset = Button(text="Reset", bg=RED, font=FONT_NAME, activebackground=RED, highlightthickness=0)
start.grid(column=0, row=2)
reset.grid(column=2, row=2)

# Canvas related
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(102, 112, image=tomato_img)
canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
