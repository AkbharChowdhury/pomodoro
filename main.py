from colour import Colours
from schedule import Schedule
from tkinter import *

FONT_NAME = "Courier"


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def main():
    window = Tk()
    window.title('pomodoro'.title())
    window.config(padx=100, pady=50, bg=Colours.YELLOW.value)
    canvas = Canvas(width=200, height=224, bg=Colours.YELLOW.value)
    tomato_image = PhotoImage(file='tomato.png')
    canvas.create_image(103, 112, image=tomato_image)
    canvas.create_text(103, 130, text='00:00', font=(FONT_NAME, 35, 'bold'), fill='white')
    canvas.pack()
    window.mainloop()


if __name__ == '__main__':
    main()
