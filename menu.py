from src.expense import Expense
from src.file_manager import load_expenses, save_expenses, backup_data, restore_data
from src.reports import generate_summary, generate_category_summary, generate_monthly_report
from src.utils import get_user_input, validate_amount, validate_date

def display_menu():
    print("\n==========================================")
    print("   PERSONAL FINANCE MANAGER")
    print("==========================================")
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. Category-wise Summary")
    print("4. Generate Monthly Report")
    print("5. Backup Data")
    print("6. Restore Data")
    print("7. Exit")

def add_expense(expenses):
    amount = get_user_input("Enter amount: ", validate_amount)
    category = get_user_input("Enter category: ")
    date = get_user_input("Enter date (YYYY-MM-DD): ", validate_date)
    description = get_user_input("Enter description: ")
    expenses.append(Expense(amount, category, date, description))
    save_expenses(expenses)
    print("Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense}")

def run_menu():
    expenses = load_expenses()
    while True:
        display_menu()
        choice = get_user_input("Enter your choice: ")
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            generate_category_summary(expenses)
        elif choice == '4':
            year_month = get_user_input("Enter year-month (YYYY-MM): ")
            generate_monthly_report(expenses, year_month)
        elif choice == '5':
            backup_data()
        elif choice == '6':
            backup_file = get_user_input("Enter backup file path: ")
            restore_data(backup_file)
            expenses = load_expenses()  # Reload after restore
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")