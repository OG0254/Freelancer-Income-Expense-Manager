class Project(object):
    def __init__(self, name, revenue):
        self.name = name
        self.revenue = revenue
        self.expenses = []

    def add_expense(self, expense_name, amount):
        self.expenses.append((expense_name, amount))  # ✅ Adds a new expense as a (name, amount) pair to the expenses list

    def total_expenses(self):
        total = 0
        for name, amount in self.expenses:  #✅ Explanation:
            total += amount                    # Assumes each item in self.expenses is a tuple of two values, like ("Rent", 5000)
        return total                           # Unpacks it into name and amount
                                            # Adds only the amount part
        
    def calculate_net_profit(self):
        return self.revenue - self.total_expenses()

    def display_summary(self):
        print(f"Project: {self.name}")
        print(f"Revenue: {self.revenue}")
        print("Expenses:")
        for name, amount in self.expenses:
            print(f"  {name}: {amount}")
        print(f"Total Expenses: {self.total_expenses()}")
        print(f"Net Profit: {self.calculate_net_profit()}")

# project2 = Project("App Development", 100000)
# project2.add_expense("Developer Salaries", 40000)
# project2.add_expense("Software Licenses", 5000)
# project2.add_expense("Marketing", 15000)

#project2.display_summary()
