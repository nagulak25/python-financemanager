from collections import defaultdict
from datetime import datetime

def generate_summary(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return
    total = sum(e.amount for e in expenses)
    average = total / len(expenses)
    print(f"Total Expenses: {total:.2f}")
    print(f"Average Expense: {average:.2f}")

def generate_category_summary(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return
    category_totals = defaultdict(float)
    for e in expenses:
        category_totals[e.category] += e.amount
    print("Category-wise Summary:")
    for category, total in category_totals.items():
        print(f"  {category}: {total:.2f}")

def generate_monthly_report(expenses, year_month):
    if not expenses:
        print("No expenses to report.")
        return
    monthly_expenses = [e for e in expenses if e.date.startswith(year_month)]
    if not monthly_expenses:
        print(f"No expenses for {year_month}.")
        return
    total = sum(e.amount for e in monthly_expenses)
    average = total / len(monthly_expenses)
    print(f"Monthly Report for {year_month}:")
    print(f"  Total: {total:.2f}")
    print(f"  Average: {average:.2f}")
    print(f"  Number of Expenses: {len(monthly_expenses)}")