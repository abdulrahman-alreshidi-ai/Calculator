import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


expenses = load_expenses()

while True:

    print("\n========== Expense Tracker ==========")
    print("1. View Expenses")
    print("2. Add Expense")
    print("3. Delete Expense")
    print("4. Total Expenses")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":

        if not expenses:
            print("No expenses found.")

        else:
            print("\nExpenses")
            print("-" * 35)

            for index, expense in enumerate(expenses, start=1):
                print(f"{index}. {expense['title']} - ${expense['amount']}")

    elif choice == "2":

        title = input("Expense Title: ")

        try:
            amount = float(input("Amount: "))

            expenses.append({
                "title": title,
                "amount": amount
            })

            save_expenses(expenses)

            print("Expense added successfully.")

        except ValueError:
            print("Invalid amount.")

    elif choice == "3":

        if not expenses:
            print("No expenses to delete.")

        else:

            for index, expense in enumerate(expenses, start=1):
                print(f"{index}. {expense['title']}")

            try:
                number = int(input("Expense Number: "))

                if 1 <= number <= len(expenses):

                    removed = expenses.pop(number - 1)

                    save_expenses(expenses)

                    print(f"{removed['title']} deleted.")

                else:
                    print("Invalid number.")

            except ValueError:
                print("Invalid input.")

    elif choice == "4":

        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"\nTotal Expenses = ${total:.2f}")

    elif choice == "5":

        print("Goodbye.")
        break

    else:
        print("Invalid choice.")
