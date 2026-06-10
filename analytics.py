from datetime import datetime

def filter_by_periodicity(habits, periodicity):
    """
    Returns all habits that match the specified periodicity.
    """
    return [h for h in habits if h.periodicity == periodicity]


def get_most_completed(habits):
    """
    Returns the habit with the highest number of completions.
    """
    if not habits:
        return None

    return max(habits, key=lambda h: len(h.completed_dates))

def get_total_completed(habits):
    """
    Returns the total number of completed dates across all habits.
    """
    return sum(len(h.completed_dates) for h in habits)


def get_longest_streak(habits):
    """
    Returns the habit with the longest current streak.
    """
    if not habits:
        return None

    return max(habits, key=lambda h: h.get_streak())


# ____________________
# Best Streak
# ____________________

def get_best_streak(habit):
    """
    Returns the best streak for a habit.
    Daily habits are checked day by day.
    Weekly habits are checked week by week.
    """

    dates = sorted([
        datetime.strptime(date, "%Y-%m-%d").date()
        for date in habit.completed_dates
    ])

    if not dates:
        return 0

    best = 1
    current = 1

    if habit.periodicity == "daily":
        expected_gap = 1
    elif habit.periodicity == "weekly":
        expected_gap = 7
    else:
        return 0

    for i in range(1, len(dates)):
        gap = (dates[i] - dates[i - 1]).days

        if gap == expected_gap:
            current += 1
        else:
            best = max(best, current)
            current = 1

    return max(best, current)

# ____________________
# Completion Rate
# ____________________

def get_completion_rate(habit, total_days):
    """
    Calculates the completion rate of a habit as a percentage.
    """
    if total_days == 0:
        return 0

    return round((len(habit.completed_dates) / total_days) * 100, 1)

# ____________________
# Habit Performance Rating
# ____________________

def get_performance_rating(habit, total_days):
    """
    Returns a performance rating based on completion rate.
    """
    rate = get_completion_rate(habit, total_days)

    if rate >= 80:
        return "Excellent"

    elif rate >= 50:
        return "Good"

    else:
        return "Needs Improvement"

def progress_bar(rate):
    """
    Creates a text-based progress bar from a percentage value.
    """
    filled = int(rate / 10)
    empty = 10 - filled

    return "█" * filled + "░" * empty

def get_average_completion_rate(habits, total_days):
    """
    Calculates the average completion rate across all habits.
    """
    if not habits:
        return 0

    total_rate = 0

    for habit in habits:
        total_rate += get_completion_rate(habit, total_days)

    return round(total_rate / len(habits), 1)


# ____________________
# Dashboard
# ____________________

def generate_dashboard(habits, start_date, end_date):
    """
    Prints the analytics dashboard for all habits.
    """

    if not habits:
        print("No habits available.")
        return

    total_days = (end_date - start_date).days + 1

    daily_count = len(filter_by_periodicity(habits, "daily"))
    weekly_count = len(filter_by_periodicity(habits, "weekly"))
    lowest = min(habits, key=lambda habit: len(habit.completed_dates))

    print("\n📊 Statistics")
    print(f"Daily Habits: {daily_count}")
    print(f"Weekly Habits: {weekly_count}")
    print(f"Lowest Consistency Habit: {lowest.name}")
    print()

    for habit in habits:
        print(f"🔹 {habit.name}")

        rate = get_completion_rate(habit, total_days)

        print(f"📈 Completion Rate: {rate}%")
        print(f"📊 Progress: {progress_bar(rate)}")
        print(f"📊 Performance: {get_performance_rating(habit, total_days)}")

        current = habit.get_streak()
        best = habit.get_longest_streak()

        if habit.periodicity == "daily":
            current_unit = "day" if current == 1 else "days"
            best_unit = "day" if best == 1 else "days"
        else:
            current_unit = "week" if current == 1 else "weeks"
            best_unit = "week" if best == 1 else "weeks"

        print(f"🔥 Current Streak: {current} {current_unit}")
        print(f"🏆 Best Streak: {best} {best_unit}")

        badges = get_achievement_badges(habit)
        print(f"🎖️ Badges: {', '.join(badges)}")

        print()

# ____________________
# Weekly Summary
# ____________________

def generate_weekly_summary(habits):
    """
    Displays a summary of weekly habit statistics.
    """
    if not habits:
        print("No habits available for weekly summary.")
        return

    print("\n📅 Weekly Summary")

    total_completions = 0

    for habit in habits:
        total_completions += len(habit.completed_dates)

    most_completed = get_most_completed(habits)
    longest_streak = get_longest_streak(habits)

    print(f"✅ Total Habit Completions: {total_completions}")
    print(f"🏆 Most Completed Habit: {most_completed.name if most_completed else 'None'}")
    print(f"🔥 Strongest Streak: {longest_streak.name if longest_streak else 'None'}")

# ____________________
# Achievement Badges
# ____________________

def get_achievement_badges(habit):
    """
    Returns achievement badges earned by a habit.
    """
    badges = []

    completions = len(habit.completed_dates)
    streak = habit.get_streak()

    if streak >= 7:
        badges.append("🏅 7-Day Streak")

    if streak >= 3:
        badges.append("🔥 3-Day Streak")

    if completions >= 20:
        badges.append("⭐ 20+ Completions")

    if habit.periodicity == "weekly" and streak >= 4:
        badges.append("📅 Monthly Consistency")

    if not badges:
        badges.append("Keep going!")

    return badges


def generate_insight(habits):
    """
    Generates a short text insight based on the user's habits.
    """

    if not habits:
        return "No habits have been added yet."

    most_completed = get_most_completed(habits)

    daily_habits = filter_by_periodicity(habits, "daily")
    weekly_habits = filter_by_periodicity(habits, "weekly")

    return (
        f"Your strongest habit is '{most_completed.name}'. "
        f"You currently have {len(daily_habits)} daily habits and "
        f"{len(weekly_habits)} weekly habits being tracked."
    )
def print_summary(habits):
    """
    Prints a summary of key habit analytics.
    """

    most = get_most_completed(habits)
    total = get_total_completed(habits)

    print("🏆 Summary")
    print(f"Most Completed Habit: {most.name if most else 'None'}")
    print(f"Total Completions: {total}")

    print("\n💡 Insight:")
    print(generate_insight(habits))

# ____________________
# Export Analytics Report
# ____________________

def export_report(habits, total_days):
    """
    Exports habit analytics to a text file report.
    """

    with open("analytics_report.txt", "w") as file:

        file.write("HABIT TRACKER ANALYTICS REPORT\n")
        file.write("=" * 40 + "\n\n")

        for habit in habits:

            rate = get_completion_rate(habit, total_days)

            file.write(f"Habit: {habit.name}\n")
            file.write(f"Periodicity: {habit.periodicity}\n")
            file.write(f"Completion Rate: {rate}%\n")
            file.write(f"Current Streak: {habit.get_streak()}\n")
            file.write(f"Best Streak: {habit.get_longest_streak()}\n")
            file.write("\n")

    print("📄 Analytics report exported successfully!")
