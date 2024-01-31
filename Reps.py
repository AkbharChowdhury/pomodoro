from enum import Enum
from schedule import Schedule


# class  Rep
class Reps:
    def __init__(self):
        self.__reps = 0

    @property
    def reps(self):
        return self.__reps

    def increment_reps(self):
        self.__reps += 1

    def reset_reps(self):
        self.__reps = 0

    def calculate_reps(self):
        is_long_break = self.__reps % 8 == 0
        is_short_break = self.__reps % 2 == 0
        if is_long_break:
            return Schedule.LONG_BREAK_MIN
        if is_short_break:
            return Schedule.SHORT_BREAK_MIN
        return Schedule.WORK_MIN
