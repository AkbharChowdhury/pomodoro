from colour import Colours
from countdown import CountDown
from schedule import Schedule
from tkinter import *
import time

FONT_NAME = "Courier"
HEIGHT = 100
BACKGROUND_COLOUR = Colours.YELLOW.value
CHECK_MARK = '✔'
win = None
from dataclasses import dataclass


# ---------------------------- TIMER RESET ------------------------------- #


# def count_down(count):
#     print(count)
#     win.
#     win.after(1_000,count_down, count - 1)
# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def main():
    window = Tk()

    window.title('pomodoro'.title())
    window.config(padx=HEIGHT, pady=50, bg=BACKGROUND_COLOUR)
    title_label = Label(text='timer'.capitalize(), fg=Colours.GREEN.value, font=(FONT_NAME, 50),
                        bg=BACKGROUND_COLOUR)
    title_label.grid(row=0, column=1)
    canvas = Canvas(width=200, height=224, bg=BACKGROUND_COLOUR, highlightthickness=0)
    tomato_image = PhotoImage(file='tomato.png')
    canvas.create_image(HEIGHT, 112, image=tomato_image)
    timer_label = canvas.create_text(HEIGHT, 130, text='00:00', font=(FONT_NAME, 35, 'bold'), fill='white')

    canvas.grid(column=1, row=1)
    timer = CountDown(window=window, canvas=canvas, label=timer_label)

    start_button = Button(text='start'.capitalize(), highlightthickness=0, highlightbackground=BACKGROUND_COLOUR,
                          command= lambda: timer.start(300))
    start_button.grid(column=0, row=2)

    reset_button = Button(text='reset'.capitalize(), highlightthickness=0, highlightbackground=BACKGROUND_COLOUR)
    reset_button.grid(column=2, row=2)

    check_marks = Label(text=CHECK_MARK, fg=Colours.GREEN.value, bg=BACKGROUND_COLOUR)
    check_marks.grid(row=3, column=1)
    window.resizable(False, False)

    window.mainloop()


if __name__ == '__main__':
    main()
    import datetime


