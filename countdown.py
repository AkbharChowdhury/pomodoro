from dataclasses import dataclass
from tkinter import Tk, Canvas, Label


@dataclass(frozen=True, slots=True)
class CountDown:
    window: Tk
    canvas: Canvas
    label: int

    def start(self):
        self.countdown(5)

    def countdown(self, count):
        self.canvas.itemconfig(self.label, text=count)
        if count > 0:
            print(count)
            self.window.after(1000, self.countdown, count - 1)