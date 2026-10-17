import datetime
expences = []

def add_expense(name, amount, category):
        dict_expences = {
            "name": name,
            "amount": amount,
            "category": category,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        expences.append(dict_expences)
def display_expenses():
        for expense in expences:
            print(f"Expense Name: {expense['name']}")
            print(f"Expense Amount: {expense['amount']}")
            print(f"Expense Category: {expense['category']}")
            print(f"Expense Date: {expense['date']})")
def calculate_total():
        total = 0
        for expense in expences:
            total += expense['amount']
        return total
while True:
    name = input("Enter the name of expense: ")
    while True:
       try:
                 amount = int(input("Enter the amount of expense: "))
                 break 
       except ValueError:
                 print("Invalid input! Please enter a number for the amount.")
    category = input("Enter the category of expense: ") 
    add_expense(name, amount, category)
    display_expenses()
    total = calculate_total()
    print(f"Total Expenses: {total}")
    
    continue_input = input("Do you want to add another expense? (y/n): ")
    if continue_input.lower() != 'y':
        break