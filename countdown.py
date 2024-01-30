from dataclasses import dataclass
import datetime
from tkinter import Tk, Canvas, Label


@dataclass(frozen=True, slots=True)
class CountDown:
    window: Tk
    canvas: Canvas
    label: int

    def start(self, num_seconds: int):
        self.countdown(num_seconds)

    def countdown(self, num_seconds):
        time_format = str(datetime.timedelta(seconds=num_seconds))

        self.canvas.itemconfig(self.label, text=time_format)
        if num_seconds > 0:
            self.window.after(1000, self.countdown, num_seconds - 1)