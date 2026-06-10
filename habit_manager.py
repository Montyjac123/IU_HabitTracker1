from habit import Habit


class HabitManager:
    def __init__(self):
        """
        Creates a habit manager with an empty habit list.
        """
        self.habits = []

    def add_habit(self, name, periodicity):
        """
        Adds a new habit to the habit list.
        """
        self.habits.append(Habit(name, periodicity))

    def list_habits(self):
        """
        Returns the list of all habits.
        """
        return self.habits

    def complete_habit(self, index):
        """
        Marks a habit as complete using its index.
        """
        if 0 <= index < len(self.habits):
            return self.habits[index].mark_completed()

        return False

    def edit_habit(self, index, new_name, new_periodicity):
        """
        Edits the name and periodicity of an existing habit.
        """
        if 0 <= index < len(self.habits):
            self.habits[index].name = new_name
            self.habits[index].periodicity = new_periodicity
            return True

        return False

    def delete_habit(self, index):
        """
        Deletes a habit using its index.
        """
        if 0 <= index < len(self.habits):
            del self.habits[index]
            return True

        return False

