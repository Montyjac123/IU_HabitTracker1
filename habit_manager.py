from habit import Habit


class HabitManager:
    def __init__(self):
        self.habits = []

    def add_habit(self, name, periodicity):
        self.habits.append(Habit(name, periodicity))

    def list_habits(self):
        return self.habits

    def complete_habit(self, index):
        if 0 <= index < len(self.habits):
            return self.habits[index].mark_completed()

        return False

