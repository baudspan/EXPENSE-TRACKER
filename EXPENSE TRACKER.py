from collections import defaultdict
from colorama import Fore, Back, Style, init
init(autoreset=True)

import json
from datetime import datetime
FILENAME = "expenses.json"
expenses = []

def load_expenses():
    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses():
    with open(FILENAME, 'w') as file:
        json.dump(expenses, file, indent=4)

def menu():
    global expenses
    expenses = load_expenses()
    while True:  
        print(Fore.CYAN + Style.BRIGHT +"\n--- Expense Tracker ---")
        print(Fore.LIGHTCYAN_EX +"1. Add Expense")
        print(Fore.LIGHTCYAN_EX +"2. View Summaries")
        print(Fore.LIGHTCYAN_EX +"3. Exit")
        choice =int(input( Fore.BLACK + "Enter your choice: "))

        if choice == 1:
            add_expense()  
        elif choice == 2:
            view_summary() 
        elif choice == 3:
            save_expenses()
            print(Fore.GREEN +"👋 Exiting. Your data is saved!")
            break  # break out of the loop
        else:
            print(Fore.RED+"❌ Invalid input. Try again.")
def add_expense():
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    while True:
        print("enter expenses type ok if done")
        category = input("Enter category (Food, Transport, etc.): ")
        if category.lower()=='ok':
            break
        try:
            amount = float(input("Amount for {}: ₹".format(category)))
        except ValueError:
            print(Fore.RED+"❌ Please enter a valid amount.")
            continue
    
        expense={
            "amount":amount,
            "category":category,
            "date":date
        }
        expenses.append(expense)
    save_expenses()
    print("expense added")
def view_summary():
    if not expenses:
            print("😢 No expenses to show yet.")
            return
    total_spent = 0
    category_totals = defaultdict(float)
    daily_totals = defaultdict(float)
    monthly_totals = defaultdict(float)

    for exp in expenses:
        amt = exp["amount"]
        cat = exp["category"]
        date_str = exp["date"]
        month = date_str[:7]

        total_spent += amt
        category_totals[cat] += amt
        daily_totals[date_str] += amt
        monthly_totals[month] += amt

    # Total & Category Breakdown
    print(Fore.MAGENTA + f"\n📊 Total Spending: ₹{total_spent:.2f}")
    print(Fore.CYAN + "\n🗂️ Category-wise Breakdown:")
    for cat, amt in category_totals.items():
        print(Fore.LIGHTBLUE_EX + f"  - {cat}: ₹{amt:.2f}")

    # Monthly Summary
    print(Fore.YELLOW + "\n📅 Monthly Spending:")
    for month, amt in sorted(monthly_totals.items()):
        print(Fore.LIGHTCYAN_EX + f"  {month}: ₹{amt:.2f}")

    # Daily Summary
    print(Fore.YELLOW + "\n🗓 Daily Spending:")
    for date, amt in sorted(daily_totals.items()):
        print(Fore.LIGHTMAGENTA_EX + f"  {date}: ₹{amt:.2f}")
        
if __name__ == "__main__":
    print(Fore.BLUE + Style.BRIGHT + "\n🌟 Welcome to your Personal Expense Tracker 🌟")
    menu()