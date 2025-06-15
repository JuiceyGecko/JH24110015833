import sqlite3

def create_tables():
    """Create necessary database tables."""
    conn = sqlite3.connect("budget_tracker.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL COLLATE NOCASE,
        amount REAL NOT NULL,
        date TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS income (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL COLLATE NOCASE,
        amount REAL NOT NULL,
        date TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS budgets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT UNIQUE NOT NULL COLLATE NOCASE,
        budget REAL NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS goals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        goal TEXT NOT NULL,
        target REAL NOT NULL,
        progress REAL DEFAULT 0
    )''')

    conn.commit()
    conn.close()

def sanitize_input(prompt, input_type=float):
    """Sanitize user input and handle errors."""
    while True:
        try:
            user_input = input(prompt)
            if input_type == float:
                user_input = user_input.replace('R', '').replace(',', '')
            return input_type(user_input)
        except ValueError:
            print("Invalid input. Please try again.")

def add_expense():
    """Add a new expense to the database."""
    category = input("Enter expense category: ").strip()
    amount = sanitize_input("Enter expense amount: ", float)
    date = input("Enter date (YYYY-MM-DD): ").strip()

    conn = sqlite3.connect("budget_tracker.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (category, amount, date) VALUES (?, ?, ?)", (category, amount, date))
    conn.commit()
    conn.close()
    print("Expense added successfully.")

def view_expenses():
    """View all expenses."""
    conn = sqlite3.connect("budget_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()

    if rows:
        print("Expenses:")
        for row in rows:
            print(f"ID: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Date: {row[3]}")
    else:
        print("No expenses found.")

def view_expenses_by_category():
    """View expenses filtered by category."""
    category = input("Enter category to filter by: ").strip()

    conn = sqlite3.connect("budget_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE category = ? COLLATE NOCASE", (category,))
    rows = cursor.fetchall()
    conn.close()

    if rows:
        print(f"Expenses in category '{category}':")
        for row in rows:
            print(f"ID: {row[0]}, Amount: {row[2]}, Date: {row[3]}")
    else:
        print(f"No expenses found in category '{category}'.")

def add_income():
    """Add new income to the database."""
    category = input("Enter income category: ").strip()
    amount = sanitize_input("Enter income amount: ", float)
    date = input("Enter date (YYYY-MM-DD): ").strip()

    conn = sqlite3.connect("budget_tracker.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO income (category, amount, date) VALUES (?, ?, ?)", (category, amount, date))
    conn.commit()
    conn.close()
    print("Income added successfully.")

def view_income():
    """View all income."""
    conn = sqlite3.connect("budget_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM income")
    rows = cursor.fetchall()
    conn.close()

    if rows:
        print("Income:")
        for row in rows:
            print(f"ID: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Date: {row[3]}")
    else:
        print("No income found.")

def view_income_by_category():
    """View income filtered by category."""
    category = input("Enter category to filter by: ").strip()

    conn = sqlite3.connect("budget_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM income WHERE category = ? COLLATE NOCASE", (category,))
    rows = cursor.fetchall()
    conn.close()

    if rows:
        print(f"Income in category '{category}':")
        for row in rows:
            print(f"ID: {row[0]}, Amount: {row[2]}, Date: {row[3]}")
    else:
        print(f"No income found in category '{category}'.")

def set_budget():
    """Set a budget for a specific category."""
    category = input("Enter category: ").strip()
    budget = sanitize_input("Enter budget amount: ", float)

    conn = sqlite3.connect("budget_tracker.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO budgets (category, budget) VALUES (?, ?) ON CONFLICT(category) DO UPDATE SET budget = ?", (category, budget, budget))
    conn.commit()
    conn.close()
    print("Budget set successfully.")

def view_budget():
    """View budget for a specific category."""
    category = input("Enter category: ").strip()

    conn = sqlite3.connect("budget_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT budget FROM budgets WHERE category = ? COLLATE NOCASE", (category,))
    row = cursor.fetchone()
    conn.close()

    if row:
        print(f"Budget for category '{category}': {row[0]}")
    else:
        print(f"No budget found for category '{category}'.")

def set_financial_goal():
    """Set a financial goal."""
    goal = input("Enter goal description: ").strip()
    target = sanitize_input("Enter target amount: ", float)

    conn = sqlite3.connect("budget_tracker.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO goals (goal, target) VALUES (?, ?)", (goal, target))
    conn.commit()
    conn.close()
    print("Financial goal set successfully.")

def view_financial_goals():
    """View progress towards financial goals."""
    conn = sqlite3.connect("budget_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT goal, target, progress FROM goals")
    rows = cursor.fetchall()
    conn.close()

    if rows:
        print("Financial Goals:")
        for row in rows:
            print(f"Goal: {row[0]}, Target: {row[1]}, Progress: {row[2]}")
    else:
        print("No financial goals found.")

def main():
    """Main program loop."""
    create_tables()

    while True:
        print("\nMenu:")
        print("1. Add expense")
        print("2. View expenses")
        print("3. View expenses by category")
        print("4. Add income")
        print("5. View income")
        print("6. View income by category")
        print("7. Set budget for a category")
        print("8. View budget for a category")
        print("9. Set financial goals")
        print("10. View progress towards financial goals")
        print("11. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_expenses_by_category()
        elif choice == "4":
            add_income()
        elif choice == "5":
            view_income()
        elif choice == "6":
            view_income_by_category()
        elif choice == "7":
            set_budget()
        elif choice == "8":
            view_budget()
        elif choice == "9":
            set_financial_goal()
        elif choice == "10":
            view_financial_goals()
        elif choice == "11":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
