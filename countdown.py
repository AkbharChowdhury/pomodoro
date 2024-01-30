from dataclasses import dataclass
from tkinter import Tk, Canvas, Label


@dataclass(frozen=True, slots=True)
class CountDown:
    window: Tk
    canvas: Canvas
    label: int

    def start(self, num_seconds: int):
        self.countdown(num_seconds)

    def countdown(self, count):
        self.canvas.itemconfig(self.label, text=count)
        if count > 0:
            print(count)
            self.window.after(1000, self.countdown, count - 1)