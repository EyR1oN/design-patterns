import random
from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def get_data(self):
        pass


class WorkHome(Strategy):
    time = "on free schedule"

    def get_data(self):
        return "work at home", self.time


class UsualWork(Strategy):
    time = "9:00-18:00"

    def get_data(self):
        return "work on weekdays", self.time


class WorkOnWeekends(Strategy):
    time = "9:00-13:00"

    def get_data(self):
        return "work on weekends", self.time


class Teacher:
    strategy: Strategy

    def __init__(self, name: str, strategy: Strategy = None) -> None:
        self.name = name
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = self.choose_strategy()

    @staticmethod
    def choose_strategy():
        return random.choice([WorkHome(), UsualWork(), WorkOnWeekends()])
    
    def __str__(self) -> str:
        str_, time = self.strategy.get_data()

        return "Dear " + self.name + "!\n" + "You should " + str_ + " " + time + " this week.\n"


teacher = Teacher("Oleg")
print(teacher)

teacher1 = Teacher("Ivan")
print(teacher1)

teacher2 = Teacher("Lesia")
print(teacher2)

teacher3 = Teacher("Stepan")
print(teacher3)
