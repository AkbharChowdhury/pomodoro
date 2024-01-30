from dataclasses import dataclass
import datetime
from tkinter import Tk, Canvas, Label

from colour import Colours
from schedule import Schedule


@dataclass(frozen=False, slots=True)
class CountDown:
    window: Tk
    canvas: Canvas
    timer_label: int
    title_label: Label
    reps: int = 0

    def change_text(self, title: str, colour: str = Colours.GREEN.value):
        self.title_label.config(text=title.capitalize(), fg=colour, font=("Courier", 50),
                                bg=Colours.YELLOW.value)

    def start(self):
        # reps = self.reps
        self.reps += 1
        work_sec = self.__as_seconds(Schedule.WORK_MIN)
        short_break_sec = self.__as_seconds(Schedule.SHORT_BREAK_MIN)
        long_break_sec = self.__as_seconds(Schedule.LONG_BREAK_MIN)

        is_long_break = self.reps % 8 == 0
        is_short_break = self.reps % 2 == 0


        self.countdown(work_sec)

        if is_long_break:
            self.countdown(long_break_sec)
            self.change_text('long break', Colours.RED.value)

        elif is_short_break:
            self.countdown(short_break_sec)
            # self.change_text('short break', Colours.PINK.value)

        else:
            self.countdown(work_sec)
            # self.change_text('work')

    def countdown(self, num_seconds):
        time_format = str(datetime.timedelta(seconds=num_seconds))

        self.canvas.itemconfig(self.timer_label, text=time_format)
        if num_seconds > 0:
            self.window.after(1000, self.countdown, num_seconds - 1)
        else:
            self.start()

    @staticmethod
    def __as_seconds(work_type: Schedule):
        return work_type.value * 60
