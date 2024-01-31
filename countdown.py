import math
from dataclasses import dataclass
import datetime
from tkinter import Tk, Canvas, Label

from colour import Colours
from schedule import Schedule


@dataclass()
class CountDown:
    window: Tk
    canvas: Canvas
    timer_label: int
    title_label: Label
    check_mark_label: Label

    reps: int = 0
    CHECK_MARK = '✔'
    timer = None

    def reset(self):
        self.window.after_cancel(self.timer)
        self.canvas.itemconfig(self.timer_label, text='00:00')
        self.__change_title_text('timer', Colours.GREEN.value)
        self.check_mark_label.config(text='')
        self.reps = 0

    def __change_title_text(self, title: str, colour: str):
        self.title_label.config(text=title.capitalize(), fg=colour)

    def start(self):
        self.reps += 1

        work_sec = CountDown.as_seconds(Schedule.WORK_MIN)
        short_break_sec = CountDown.as_seconds(Schedule.SHORT_BREAK_MIN)
        long_break_sec = CountDown.as_seconds(Schedule.LONG_BREAK_MIN)

        is_long_break = self.reps % 8 == 0
        is_short_break = self.reps % 2 == 0

        if is_long_break:
            self.__change_title_text('long break', Colours.RED.value)
            self.countdown(long_break_sec)
            return

        if is_short_break:
            self.__change_title_text('short break', Colours.PINK.value)
            self.countdown(short_break_sec)
            return

        self.__change_title_text('work', Colours.GREEN.value)
        self.countdown(work_sec)

    def countdown(self, num_seconds):
        time_format = str(datetime.timedelta(seconds=num_seconds))
        self.canvas.itemconfig(self.timer_label, text=time_format)
        if num_seconds > 0:
            self.timer = self.window.after(1000, self.countdown, num_seconds - 1)
        else:
            self.start()
            self.check_mark_label.config(text=self.__marks())
            print(self.__marks())

    def __marks(self):
        work_sessions = int(math.floor(self.reps / 2))
        marks = [CountDown.CHECK_MARK for _ in range(work_sessions)]
        return "".join(marks)

    @staticmethod
    def as_seconds(work_type: Schedule):
        return work_type.value * 60
