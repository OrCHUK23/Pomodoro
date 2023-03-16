from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.3
reps = 0
my_timer = None
check_mark_text = ""

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(my_timer)
    title_label.config(text="Timer", bg=YELLOW, fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 1st/3rd/5th/7th rep, then do 25 minutes work:
    if reps < 9:
        if reps % 2 != 0:
            title_label.config(text="Work", fg=GREEN)
            count_down(work_sec)
        # If it's the 8th rep do 20 minutes long break.
        elif reps % 8 == 0:
            title_label.config(text="Break", fg=RED)
            count_down(long_break_sec)
        # If it's 2nd/4th/6th rep do a 5 minutes short break timer.
        else:
            title_label.config(text="Break", fg=PINK)
            count_down(short_break_sec)
    else:
        # TODO: ADD DONE MESSAGE.
        pass

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # Convert to minutes layout timer.
    count_min = math.floor(count / 60)
    count_sec = count % 60
    global reps

    # Treatment of "00" the end of the timer.
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # Display the timer on the screen.
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    # Handling the timer backward countdown.
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    else:  # Start the timer again after countdown reached 0.
        start_timer()
        if reps % 2 == 0:
            # Handling check marks drawing.
            global check_mark_text
            for _ in range(math.floor(reps/2)):
                check_mark_text += "✓"
            check_marks_label.config(text=check_mark_text)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Program")
window.config(padx=100, pady=50, bg=YELLOW)
window.minsize(width=400, height=400)

# Timer label.
title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(row=0, column=1)

# Tomato image + timer text.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Start button.
start_button = Button(text="Start", command=start_timer, borderwidth=0.5, highlightthickness=0)
start_button.grid(row=2, column=0)

# Reset button.
reset_button = Button(text="Reset", command=reset_timer, borderwidth=0.5, highlightthickness=0)
reset_button.grid(row=2, column=2)

# Check marks labels.
check_marks_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
check_marks_label.grid(row=3, column=1)

window.mainloop()
