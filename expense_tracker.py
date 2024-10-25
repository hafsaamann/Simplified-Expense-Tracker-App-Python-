# expense_tracker.py

expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    expenses.append((name, amount))
    print(f"Added: {name} - ${amount}")

def show_expenses():
    print("\n--- Expenses ---")
    for name, amount in expenses:
        print(f"{name}: ${amount}")

def total_expenses():
    total = sum(amount for name, amount in expenses)
    print(f"Total expenses: ${total}")

while True:
    print("\n[1] Add Expense  [2] Show Expenses  [3] Show Total  [4] Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        break
