import math
from dataclasses import dataclass
import datetime
from tkinter import Tk, Canvas, Label

from Reps import Reps
from colour import Colours
from schedule import Schedule
from symbol import Symbol


@dataclass()
class CountDown:
    window: Tk
    canvas: Canvas
    timer_label: int
    title_label: Label
    check_mark_label: Label

    timer = None
    __reps: Reps = Reps()

    def reset(self):
        self.window.after_cancel(self.timer)
        self.canvas.itemconfig(self.timer_label, text='00:00')
        self.__change_title_text('timer', Colours.GREEN.value)
        self.check_mark_label.config(text='')
        self.__reps.reset_reps()

    def __change_title_text(self, title: str, colour: str):
        self.title_label.config(text=title.capitalize(), fg=colour)

    def start(self):
        self.__reps.increment_reps()
        self.__render_interface()

    def __render_interface(self):
        sessions = CountDown.__get_sessions()
        if self.__reps.calculate_reps() == Schedule.LONG_BREAK_MIN:
            self.__change_title_text('long break', Colours.RED.value)
            self.countdown(sessions['long_break_sec'])
            return

        if self.__reps.calculate_reps() == Schedule.SHORT_BREAK_MIN:
            self.__change_title_text('short break', Colours.PINK.value)
            self.countdown(sessions['short_break_sec'])
            return

        self.__change_title_text('work', Colours.GREEN.value)
        self.countdown(sessions['work_sec'])

    def countdown(self, num_seconds):
        time_format = str(datetime.timedelta(seconds=num_seconds))
        self.canvas.itemconfig(self.timer_label, text=time_format)
        if num_seconds > 0:
            self.timer = self.window.after(1000, self.countdown, num_seconds - 1)
            return
        self.start()
        self.check_mark_label.config(text=self.__marks())

    def __marks(self):
        """
        After every 2 reps a check mark is added
        """
        work_sessions = int(math.floor(self.__reps.reps / 2))
        marks = [Symbol.CHECK_MARK.value for _ in range(work_sessions)]
        return "".join(marks)

    @staticmethod
    def __as_seconds(work_type: Schedule):
        return work_type.value * 60

    @staticmethod
    def __get_sessions():
        return dict(
            work_sec=CountDown.__as_seconds(Schedule.WORK_MIN),
            short_break_sec=CountDown.__as_seconds(Schedule.SHORT_BREAK_MIN),
            long_break_sec=CountDown.__as_seconds(Schedule.LONG_BREAK_MIN)
        )
