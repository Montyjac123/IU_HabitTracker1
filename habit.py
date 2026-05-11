from datetime import datetime, timedelta


class Habit:
    def __init__(self, name, periodicity):
        self.name = name
        self.periodicity = periodicity
        self.created_at = datetime.now()
        self.completed_dates = []

    def mark_completed(self):
        today = datetime.now().date().isoformat()

        if today in self.completed_dates:
            return False

        self.completed_dates.append(today)
        return True

    def get_streak(self):
        if not self.completed_dates:
            return 0

        dates = sorted(
            [datetime.fromisoformat(d).date() for d in self.completed_dates],
            reverse=True
        )

        streak = 1

        for i in range(len(dates) - 1):
            difference = (dates[i] - dates[i + 1]).days

            if self.periodicity == "daily" and difference == 1:
                streak += 1
            elif self.periodicity == "weekly" and difference <= 7:
                streak += 1
            else:
                break

        return streak

    def get_longest_streak(self):
        if not self.completed_dates:
            return 0

        dates = sorted(
            [datetime.fromisoformat(d).date() for d in self.completed_dates]
        )

        longest = 1
        current = 1

        for i in range(1, len(dates)):
            difference = (dates[i] - dates[i - 1]).days

            if self.periodicity == "daily" and difference == 1:
                current += 1
                longest = max(longest, current)

            elif self.periodicity == "weekly" and difference <= 7:
                current += 1
                longest = max(longest, current)

            else:
                current = 1

        return longest
    def __str__(self):
        return f"{self.name} ({self.periodicity})"