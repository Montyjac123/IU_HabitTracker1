import json
from datetime import datetime
from habit import Habit

FILE_NAME = 'habits.json'

def save_habits(habits):
    """
    Saves the list of habits to a JSON file.
    """
    with open(FILE_NAME, "w") as f:
        json.dump([
            {
                "name": h.name,
                "periodicity": h.periodicity,
                "created_at": h.created_at.isoformat(),
                "completed_dates": h.completed_dates
            }
            for h in habits
        ], f, indent=4)

def load_habits():
    """
    Loads habits from the JSON file.
    Returns an empty list if the file does not exist or is invalid.
    """
    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)

            habits = []

            for h in data:
                habit = Habit(h["name"], h["periodicity"])
                habit.created_at = datetime.fromisoformat(h["created_at"])
                habit.completed_dates = h["completed_dates"]
                habits.append(habit)

            return habits

    except (FileNotFoundError, json.JSONDecodeError):
        return []


