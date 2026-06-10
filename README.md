# Habit Tracking App

## Overview

The Habit Tracking App is a command-line application built in Python. It helps users create, manage, and track daily and weekly habits.

Users can record habit completions, monitor streaks, analyse progress, and save their data using JSON storage.

---

## Features

- Create daily and weekly habits
- Edit existing habits
- Delete habits
- Mark habits as completed
- Track current streaks
- Track longest streaks
- Filter habits by periodicity
- Search for habits
- Generate an analytics dashboard
- Generate a weekly summary
- Export an analytics report
- Save and load data using JSON

---

## Project Structure

```text
habit.py              # Habit class and streak calculations
habit_manager.py      # Habit creation, editing and deletion
analytics.py          # Analytics functions and reporting
storage.py            # JSON saving and loading
cli.py                # Command-line interface
main.py               # Application entry point
test_habit_tracker.py # Unit tests
habits.json           # Predefined habit data

---

## Analytics

The application includes several analytics functions that help users understand their habit performance.

### Core Analytics Functions

- Filter habits by periodicity (daily or weekly)
- Find the most completed habit
- Calculate total habit completions
- Find the habit with the longest streak

### Additional Analytics Features

- Completion rate calculation
- Performance ratings
- Achievement badges
- Weekly summaries
- Habit insights
- Analytics report export

---

## Installation

Install the required dependencies:

```shell
pip install -r requirements.txt
```

---

## Usage

Run the application:

```shell
python main.py
```

Then follow the menu options shown in the terminal.

---

## Testing

The project includes unit tests for:

### Habit Management

- Habit creation
- Habit editing
- Habit deletion

### Analytics

- Filter habits by periodicity
- Most completed habit
- Total habit completions
- Longest streak
- Best streak calculations

Run the tests using:

```shell
python -m unittest test_habit_tracker.py
```
---

## Technologies Used

- Python
- JSON
- Colorama
- Unittest

---

## Screenshots

Include screenshots showing:

1. Main menu
2. Analytics dashboard
3. Weekly summary
4. Unit test results

---

## Author

Montana Jacobs
