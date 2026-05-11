import tkinter as tk
from habit_manager import HabitManager
from storage import load_habits, save_habits

manager = HabitManager()
manager.habits = load_habits()


def refresh_habits():
    habit_list.delete(0, tk.END)

    for habit in manager.habits:
        habit_list.insert(
            tk.END,
            f"{habit.name} ({habit.periodicity}) - Completed {len(habit.completed_dates)} times"
        )


def add_habit():
    name = name_entry.get().strip()
    periodicity = periodicity_var.get()

    if not name:
        status_label.config(text="Habit name cannot be empty.")
        return

    manager.add_habit(name, periodicity)
    save_habits(manager.habits)

    name_entry.delete(0, tk.END)
    status_label.config(text=f"Habit '{name}' added.")
    refresh_habits()


def complete_habit():
    selected = habit_list.curselection()

    if not selected:
        status_label.config(text="Please select a habit first.")
        return

    index = selected[0]
    result = manager.complete_habit(index)

    if result:
        save_habits(manager.habits)
        status_label.config(text="Habit completed.")
    else:
        status_label.config(text="Habit already completed today.")

    refresh_habits()


root = tk.Tk()
root.title("Habit Tracker")
root.geometry("500x400")

title = tk.Label(root, text="Habit Tracker", font=("Arial", 18, "bold"))
title.pack(pady=10)

name_entry = tk.Entry(root, width=35)
name_entry.pack(pady=5)

periodicity_var = tk.StringVar(value="daily")

daily_radio = tk.Radiobutton(root, text="Daily", variable=periodicity_var, value="daily")
daily_radio.pack()

weekly_radio = tk.Radiobutton(root, text="Weekly", variable=periodicity_var, value="weekly")
weekly_radio.pack()

add_button = tk.Button(root, text="Add Habit", command=add_habit)
add_button.pack(pady=5)

habit_list = tk.Listbox(root, width=60)
habit_list.pack(pady=10)

complete_button = tk.Button(root, text="Complete Selected Habit", command=complete_habit)
complete_button.pack(pady=5)

status_label = tk.Label(root, text="")
status_label.pack(pady=10)

refresh_habits()

root.mainloop()
