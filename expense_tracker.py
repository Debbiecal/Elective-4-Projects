import csv
from datetime import datetime

def log_expense(amount, category, description):
    """
    Logs an expense entry into the 'expenses.csv' file.
    """
    with open('expenses.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), amount, category, description])
    print(f"Logged expense: {amount} for {category} ({description})")

def generate_report():
    """
    Reads the 'expenses.csv' file and calculates the total expenses.
    """
    total = 0
    try:
        with open('expenses.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            print("Date and Time, Amount, Category, Description")
            for row in reader:
                print(", ".join(row))  # Print each row for a detailed report
                total += float(row[1])  # Accumulate the total expense
        print(f"\nTotal Expenses: ${total:.2f}")
    except FileNotFoundError:
        print("No expenses recorded yet. Start by logging an expense.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
log_expense(50, 'Groceries', 'Bought fruits and vegetables')
log_expense(20, 'Transportation', 'Bus fare')
generate_report()
