def greet():
    print("Welcome to Expense Tracker!")

greet()

expenses = []

def add_expense(description, amount, category):
    expense = {
        "id": len(expenses) + 1,
        "description": description,
        "amount": amount,
        "category": category
    }
    expenses.append(expense)

def view_expenses():
    for expense in expenses:
        print(expense)

def delete_expense(expense_id):
    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            print("Expense deleted.")
            return

    print("Expense not found.")

add_expense("Lunch", 150, "Food")
add_expense("Bus", 40, "Travel")

view_expenses()
delete_expense(1)
view_expenses()