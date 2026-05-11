def filter_by_periodicity(habits, periodicity):
    return [h for h in habits if h.periodicity == periodicity]


def get_most_completed(habits):
    if not habits:
        return None

    return max(habits, key=lambda h: len(h.completed_dates))


def get_total_completed(habits):
    return sum(len(h.completed_dates) for h in habits)


def get_longest_streak(habits):
    if not habits:
        return None

    return max(habits, key=lambda h: h.get_streak())

from datetime import datetime

# ____________________
# Best Streak
# ____________________

def get_best_streak(habit):
    dates = sorted([
        datetime.strptime(d, "%Y-%m-%d").date()
        for d in habit.completed_dates
    ])

    if not dates:
        return 0

    best = 1
    current = 1

    for i in range(1, len(dates)):
        if (dates[i] - dates[i - 1]).days == 1:
            current += 1
        else:
            best = max(best, current)
            current = 1

    return max(best, current)

# ____________________
# Completion Rate
# ____________________

def get_completion_rate(habit, total_days):
    if total_days == 0:
        return 0

    return round((len(habit.completed_dates) / total_days) * 100, 1)
# ____________________
# Habit Performance Rating
# ____________________

def get_performance_rating(habit, total_days):
    rate = get_completion_rate(habit, total_days)

    if rate >= 80:
        return "Excellent"

    elif rate >= 50:
        return "Good"

    else:
        return "Needs Improvement"

def progress_bar(rate):
    filled = int(rate / 10)
    empty = 10 - filled

    return "█" * filled + "░" * empty

def get_average_completion_rate(habits, total_days):
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
    total_days = (end_date - start_date).days + 1


    for habit in habits:
        print(f"🔹 {habit.name}")
        rate = get_completion_rate(habit, total_days)

        rate = get_completion_rate(habit, total_days)

        print(f"📈 Completion Rate: {rate}%")
        print(f"📊 Progress: {progress_bar(rate)}")
        print(f"📊 Performance: {get_performance_rating(habit, total_days)}")
        unit = "days" if habit.periodicity == "daily" else "weeks"

        current = habit.get_streak()
        best = habit.get_longest_streak()

        if habit.periodicity == "daily":
            current_unit = "day" if current == 1 else "days"
            best_unit = "day" if best == 1 else "days"
        else:
            current_unit = "week" if current == 1 else "weeks"
            best_unit = "week" if best == 1 else "weeks"

        rate = get_completion_rate(habit, total_days)

        daily_count = len([
            h for h in habits if h.periodicity == "daily"
        ])

        weekly_count = len([
            h for h in habits if h.periodicity == "weekly"
        ])

        lowest = min(
            habits,
            key=lambda h: len(h.completed_dates)
        )

        print("\n📊 Statistics")
        print(f"Daily Habits: {daily_count}")
        print(f"Weekly Habits: {weekly_count}")
        print(f"Lowest Consistency Habit: {lowest.name}")

        print(f"🔥 Current Streak: {current} {current_unit}")
        print(f"🏆 Best Streak: {best} {best_unit}")

        badges = get_achievement_badges(habit)
        print(f"🎖️ Badges: {', '.join(badges)}")

        print()

# ____________________
# Weekly Summary
# ____________________

def generate_weekly_summary(habits):
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
    if not habits:
        return "No habits have been added yet."

    most_completed = get_most_completed(habits)

    daily_habits = filter_by_periodicity(habits, "daily")
    weekly_habits = filter_by_periodicity(habits, "weekly")

    if most_completed:
        return (
            f"Your strongest habit is'{most_completed.name}'."
            f"You currently have {len(daily_habits)} daily habits and"
            f"{len(weekly_habits)} weekly habits being tracked."
    )
    return "Keep completing abits to build stronger analytics."

    def export_report(habits, total_days):

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
