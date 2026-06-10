from habit_manager import HabitManager
from storage import save_habits, load_habits

from analytics import (
    filter_by_periodicity,
    generate_dashboard,
    generate_weekly_summary,
    export_report
)

from datetime import datetime
from colorama import Fore, Style, init

manager = HabitManager()
manager.habits = load_habits()

init(autoreset=True)

def run():
    """
    Runs the Habit Tracker command-line interface.
    Displays the menu and handles user interaction.
    """
    print(Fore.CYAN + "\nWelcome back!")

    print(
        Fore.YELLOW +
        f"You are currently tracking {len(manager.habits)} habits."
    )

    if manager.habits:

        strongest = max(
            manager.habits,
            key=lambda h: len(h.completed_dates)
        )

        print(
            Fore.GREEN +
            f"🔥 Strongest Habit: {strongest.name}"
        )
    while True:
        print(Fore.CYAN + "\n" + "=" * 35)
        print(Fore.CYAN + "        HABIT TRACKER")
        print(Fore.CYAN + "=" * 35)
        print("1. Add Habit")
        print("2. View Habits")
        print("3. Complete Habit")
        print("4. Filter Habits")
        print("5. Analytics Dashboard")
        print("6. Delete Habit")
        print("7. Weekly Summary")
        print("8. Edit Habit")
        print("9. Search Habit")
        print("10. Export Analytics Report")
        print("11. Save & Exit")
        print("=" * 35)

        choice = input("Choose: ")

        # --------------------
        # Add Habit
        # --------------------
        if choice == "1":
            name = input("Habit name: ").strip()

            if not name:
                print(Fore.RED + "❌ Habit name cannot be empty.")
                continue

            periodicity = input("daily/weekly: ").strip().lower()

            if periodicity not in ["daily", "weekly"]:
                print(Fore.RED + "❌ Invalid periodicity. Please enter 'daily' or 'weekly'.")
                continue

            manager.add_habit(name, periodicity)
            save_habits(manager.habits)
            print(f"✔ Habit '{name}' added successfully!")

        # --------------------
        # View Habits
        # --------------------
        elif choice == "2":

            if not manager.habits:

                print("No habits have been added yet.")

            else:

                for i, h in enumerate(manager.habits):
                    print(

                        f"{i}: {h} | "

                        f"Completed: {len(h.completed_dates)} times | "

                        f"Current Streak: {h.get_streak()} 🔥 | "

                        f"Longest Streak: {h.get_longest_streak()} 🏆"

                    )
        elif choice == "3":
            try:
                index = int(input("Enter the number next to the habit: "))
                result = manager.complete_habit(index)

                if result:

                    save_habits(manager.habits)

                    print(Fore.GREEN + "✔ Habit marked as completed!")

                    streak = manager.habits[index].get_streak()

                    if streak >= 7:
                        print(Fore.CYAN + "🏅 Amazing! 7-day streak achieved!")

                    elif streak >= 3:
                        print(Fore.YELLOW + "🔥 Great consistency! Keep going!")

                    else:
                        print(Fore.BLUE + "💪 Nice work building your habits!")
                else:
                    print("⚠ Habit already completed today!")
            except (ValueError, IndexError):
                print(Fore.RED + "❌ Invalid habit index!")


        elif choice == "4":

            p = input("daily/weekly: ").strip().lower()

            if p not in ["daily", "weekly"]:
                print( Fore.RED + "❌ Invalid filter. Please enter 'daily' or 'weekly'.")

                continue

            filtered = filter_by_periodicity(manager.habits, p)

            if not filtered:

                print(f"No {p} habits found.")

            else:

                for h in filtered:
                    print(h)

        # --------------------
        # Analytics Dashboard
        # --------------------
        elif choice == "5":

            start_date = datetime.strptime("2026-04-14", "%Y-%m-%d").date()

            end_date = datetime.strptime("2026-05-11", "%Y-%m-%d").date()

            generate_dashboard(manager.habits, start_date, end_date)



        elif choice == "6":

            if not manager.habits:

                print(Fore.YELLOW + "No habits available to delete.")


            else:

                for i, h in enumerate(manager.habits):
                    print(f"{i}: {h.name} ({h.periodicity})")

                try:

                    index = int(input("Enter the number next to the habit to delete: "))

                    confirm = input("Are you sure you want to delete this habit? (y/n): ").strip().lower()

                    if confirm == "y":

                        deleted_habit = manager.habits[index]

                        if manager.delete_habit(index):
                            save_habits(manager.habits)
                            print(Fore.GREEN + f"Habit '{deleted_habit.name}' deleted successfully.")
                        else:
                            print(Fore.RED + "❌ Invalid habit index!")

                    else:

                        print(Fore.YELLOW + "Deletion cancelled.")


                except (ValueError, IndexError):

                    print(Fore.RED + "❌ Invalid habit index!")

        elif choice == "7":
            generate_weekly_summary(manager.habits)

        elif choice == "8":

            if not manager.habits:
                print(Fore.YELLOW + "No habits available to edit.")

            else:
                for i, h in enumerate(manager.habits):
                    print(f"{i}: {h.name} ({h.periodicity})")

                try:
                    index = int(input("Enter the number next to the habit to edit: "))

                    habit = manager.habits[index]

                    new_name = input(
                        f"New name (leave blank to keep '{habit.name}'): "
                    ).strip()

                    new_periodicity = input(
                        f"New periodicity (daily/weekly, leave blank to keep '{habit.periodicity}'): "
                    ).strip().lower()

                    if not new_name:
                        new_name = habit.name

                    if not new_periodicity:
                        new_periodicity = habit.periodicity

                    if new_periodicity not in ["daily", "weekly"]:
                        print(Fore.RED + "❌ Invalid periodicity.")
                        continue

                    if manager.edit_habit(index, new_name, new_periodicity):
                        save_habits(manager.habits)
                        print(Fore.GREEN + "✔ Habit updated successfully!")
                    else:
                        print(Fore.RED + "❌ Invalid habit index!")

                except (ValueError, IndexError):
                    print(Fore.RED + "❌ Invalid habit index!")


        elif choice == "9":

            search = input("Enter habit name to search: ").strip().lower()

            found = False

            for h in manager.habits:

                if search in h.name.lower():

                    print(
                        Fore.GREEN +
                        f"Found: {h.name} ({h.periodicity})"
                    )

                    found = True

            if not found:
                print(
                    Fore.RED +
                    "No matching habits found."
                )

        elif choice == "10":

            start_date = datetime.strptime(
                "2026-04-14",
                "%Y-%m-%d"
            ).date()

            end_date = datetime.strptime(
                "2026-05-11",
                "%Y-%m-%d"
            ).date()

            total_days = (
                end_date - start_date
            ).days + 1

            export_report(
                manager.habits,
                total_days
            )

        elif choice == "11":

            save_habits(manager.habits)

            print("Saved. Goodbye!")

            break
        else:
            print(Fore.RED + "❌ Invalid option. Please choose 1-11.")
