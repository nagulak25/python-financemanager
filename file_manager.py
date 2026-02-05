import csv
import os
from datetime import datetime
from src.expense import Expense

DATA_FILE = 'data/expenses.csv'
BACKUP_DIR = 'data/'

def load_expenses():
    expenses = []
    if not os.path.exists(DATA_FILE):
        return expenses  # Return empty list if file doesn't exist
    try:
        with open(DATA_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(Expense(
                    float(row['Amount']),
                    row['Category'],
                    row['Date'],
                    row['Description']
                ))
    except (FileNotFoundError, ValueError, KeyError) as e:
        print(f"Error loading expenses: {e}. Starting with empty list.")
    return expenses

def save_expenses(expenses):
    try:
        with open(DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])
            for expense in expenses:
                writer.writerow([expense.date, expense.category, expense.amount, expense.description])
    except Exception as e:
        print(f"Error saving expenses: {e}")

def backup_data():
    if not os.path.exists(DATA_FILE):
        print("No data to backup.")
        return
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_DIR, f"expenses_backup_{timestamp}.csv")
    try:
        with open(DATA_FILE, 'r') as src, open(backup_file, 'w') as dst:
            dst.write(src.read())
        print(f"Data backed up to {backup_file}")
    except Exception as e:
        print(f"Backup failed: {e}")

def restore_data(backup_file):
    if not os.path.exists(backup_file):
        print("Backup file not found.")
        return
    try:
        with open(backup_file, 'r') as src, open(DATA_FILE, 'w') as dst:
            dst.write(src.read())
        print("Data restored successfully.")
    except Exception as e:
        print(f"Restore failed: {e}")