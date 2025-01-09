#Class to categorise the expenses
class ExpenseCategory:
    def __init__(self, expense_name, budget):
        self.expense_name = expense_name
        self.budget = budget
        self.expense_history = []

    #Method to add expense into expense_history
    def add_expense(self, expense_date, expense_amount, expense_description):
        self.expense_history.append({'date': expense_date, 'amount': expense_amount, 'description': expense_description})

    #Method to calculate the total expenses for the category
    def total_expenses(self):
        return sum(expense['amount'] for expense in self.expense_history)

    #Method to calculate de remaining budget
    def remaining_budget(self):
        return self.budget - self.total_expenses()

    #Method to print the expenses
    def print_expenses(self):
        for expense in self.expense_history:
            print(f'{expense['date']} {expense['amount']} {expense['description']}')

#Class to categorise the income
class IncomeCategory:
    def __init__(self, income_name):
        self.income_name = income_name
        self.income_history = []

    #Method to add income into income_history
    def add_income(self, income_date, income_amount, income_description):
        self.income_history.append({'date': income_date, 'amount': income_amount, 'description': income_description})

    # Method to calculate the total income
    def total_income(self):
        return sum(income['amount'] for income in self.income_history)

    def print_income(self):
        for income in self.income_history:
            print(f'{income['date']} {income['amount']} {income['description']}')

#Class to manage the transactions
class ExpenseManager:
    def __init__(self):
        self.expense_categories = {}
        self.income_categories = {}

    def add_expense_category(self, name, budget):
        self.expense_categories[name] = ExpenseCategory(name, budget)


    def add_income_category(self, name):

        self.income_categories[name] = IncomeCategory(name)

    def add_expense(self, category, date, amount, description):
        if category in self.expense_categories:
            self.expense_categories[category].add_expense(date, amount, description)

    def add_income(self, category, date, amount, description):
        if category in self.income_categories:
            self.income_categories[category].add_income(date, amount, description)

    def print_summary(self):
        print('\n-=-=-=-=-=-=-=-Expenses Summary-=-=-=-=-=-=-=-')
        for category in self.expense_categories.values():
            print(f'Category: {category.expense_name}')
            category.print_expenses()
            print(f'Total Expenses: {category.total_expenses()} Remaining Budget: {category.remaining_budget()}')

        print('\n-=-=-=-=-=-=-=-Income Summary-=-=-=-=-=-=-=-')
        for category in self.income_categories.values():
            print(f'Category: {category.income_name}')
            category.print_income()
            print(f'Total Income: {category.total_income()}\n')


# Example usage
manager = ExpenseManager()
manager.add_expense_category("Food", 500)
manager.add_income_category("Salary")

manager.add_expense("Food", '09/01/2025', 50, "Groceries")
manager.add_expense("Food", '09/01/2025', 30, "Dinner out")
manager.add_income("Salary", '09/01/2025', 2000, "Monthly salary")
manager.add_income("Salary", '09/01/2025', 350, "Second Job")
manager.print_summary()
