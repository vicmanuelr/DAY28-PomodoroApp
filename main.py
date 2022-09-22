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
reps = 0
counter = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global counter
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Pomodoro", fg=GREEN)
    text = ""
    check_mark.config(text=text)
    if counter:
        window.after_cancel(counter)
        counter = None

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global counter
    global reps
    if counter is None:
        reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60
        if reps == 1 or reps == 3 or reps == 5 or reps == 7:
            title.config(text="Work", fg=GREEN)
            countdown(work_sec)
        elif reps == 2 or reps == 4 or reps == 6:
            title.config(text="Short Break", fg=PINK)
            countdown(short_break_sec)
        elif reps == 8:
            title.config(text="Long Break", fg=RED)
            countdown(long_break_sec)
        else:
            reset_timer()
    else:
        reset_timer()
        start_timer()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global counter
    global reps
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        counter = window.after(1000, countdown, count - 1)
    else:
        counter = None
        start_timer()
        mark = ""
        for _ in range(0, reps//2):
            mark += "✔"
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
# Window related
window = Tk()
window.title("Pomodoro")
window.config(padx=25, pady=50, bg=YELLOW)

# Labels
title = Label(text="Pomodoro", font=(FONT_NAME, 35), bg=YELLOW, fg=GREEN, justify="center")
check_mark = Label(font=(FONT_NAME, 35), bg=YELLOW, fg=GREEN, justify="center")
title.grid(column=1, row=0)
check_mark.grid(column=1, row=3)

# Buttons
start = Button(text="Start", bg=GREEN, font=FONT_NAME, activebackground=GREEN,
               highlightthickness=0, command=start_timer)
reset = Button(text="Reset", bg=RED, font=FONT_NAME, activebackground=RED, highlightthickness=0, command=reset_timer)
start.grid(column=0, row=2)
reset.grid(column=2, row=2)

# Canvas related
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
