from colour import Colours
from schedule import Schedule
from tkinter import *

FONT_NAME = "Courier"
HEIGHT = 100
BACKGROUND_COLOUR = Colours.YELLOW.value
CHECK_MARK = '✔'

# ---------------------------- TIMER RESET ------------------------------- #

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
    canvas.create_text(HEIGHT, 130, text='00:00', font=(FONT_NAME, 35, 'bold'), fill='white')
    canvas.grid(column=1, row=1)

    start_button = Button(text='start'.capitalize(), highlightthickness=0, highlightbackground=BACKGROUND_COLOUR)
    start_button.grid(column=0, row=2)

    reset_button = Button(text='reset'.capitalize(), highlightthickness=0, highlightbackground=BACKGROUND_COLOUR)
    reset_button.grid(column=2, row=2)

    check_marks = Label(text=CHECK_MARK, fg=Colours.GREEN.value, bg=BACKGROUND_COLOUR)
    check_marks.grid(row=3, column=1)
    window.mainloop()


if __name__ == '__main__':
    main()
