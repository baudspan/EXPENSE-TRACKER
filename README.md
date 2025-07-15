# EXPENSE-TRACKER
A command-line based expense tracking tool built with Python. It allows users to log daily expenses, categorize them, and view summaries by day, month, and category. Data is stored locally in a JSON file.
## Features

- Add expenses with category and date
- View total, daily, monthly, and category-wise summaries
- Automatically saves and loads data from `expenses.json`
- Color-coded terminal output using `colorama`
- Simple and interactive CLI menu

## Technologies Used

- Python 3
- `colorama` for colored terminal output
- `json` for data storage
- `datetime` for date handling
- `collections.defaultdict` for summaries

## Installation
git clone https://github.com/baudspan/EXPENSE-TRACKER.git
cd expense-tracker
pip install colorama

## ON RUNNING
python expense_tracker.py
Choose from the menu:
-Add Expenses
-View Summaries
-Exit (automatically saves data)

To log expenses:
-Enter categories and corresponding amounts
-Type ok when you're done adding for the day
-Your data is saved to expenses.json. To analyze your expenses, use the View Summaries option in the menu.

## example format
{"amount": 200.0,
"category": "Transport",
"date": "2025-07-15"}

Built by SUDEEPA Feel free to fork, contribute, or star the repo!
  



