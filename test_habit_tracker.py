import unittest

from habit import Habit
from habit_manager import HabitManager
from analytics import (
    filter_by_periodicity,
    get_most_completed,
    get_total_completed,
    get_longest_streak,
    get_best_streak
)

class TestHabitManager(unittest.TestCase):
    def test_add_habit(self):
        manager = HabitManager()
        manager.add_habit("Drink Water", "daily")

        self.assertEqual(len(manager.habits),1)
        self.assertEqual(manager.habits[0].name, "Drink Water")
        self.assertEqual(manager.habits[0].periodicity, "daily")

    def test_edit_habit(self):
        manager = HabitManager()
        manager.add_habit("Drink Water", "daily")

        result = manager.edit_habit(0,"Exercise", "weekly")

        self.assertTrue(result)
        self.assertEqual(manager.habits[0].name, "Exercise")
        self.assertEqual(manager.habits[0].periodicity, "weekly")

    def test_delete_habit(self):
        manager = HabitManager()
        manager.add_habit("Drink Water", "daily")

        result = manager.delete_habit(0)

        self.assertTrue(result)
        self.assertEqual(len(manager.habits), 0)

class TestAnalytics(unittest.TestCase):

    def setUp(self):
        self.daily_habit = Habit("Drink Water", "daily")
        self.daily_habit.completed_dates = [
            "2026-05-01",
            "2026-05-02",
            "2026-05-03"
        ]

        self.weekly_habit = Habit("Meal Prep", "weekly")
        self.weekly_habit.completed_dates = [
            "2026-05-01",
            "2026-05-08",
            "2026-05-15",
            "2026-05-22"
        ]

        self.habits = [self.daily_habit, self.weekly_habit]

    def test_filter_by_periodicity(self):
        daily_habits = filter_by_periodicity(self.habits, "daily")
        weekly_habits = filter_by_periodicity(self.habits, "weekly")

        self.assertEqual(len(daily_habits), 1)
        self.assertEqual(daily_habits[0].name, "Drink Water")

        self.assertEqual(len(weekly_habits), 1)
        self.assertEqual(weekly_habits[0].name, "Meal Prep")

    def test_get_most_completed(self):
        result = get_most_completed(self.habits)

        self.assertEqual(result.name, "Meal Prep")

    def test_get_total_completed(self):
        result = get_total_completed(self.habits)

        self.assertEqual(result, 7)

    def test_get_longest_streak(self):
        result = get_longest_streak(self.habits)

        self.assertEqual(result.name, "Meal Prep")

    def test_get_best_streak_daily(self):
        result = get_best_streak(self.daily_habit)

        self.assertEqual(result, 3)

    def test_get_best_streak_weekly(self):
        result = get_best_streak(self.weekly_habit)

        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()

