from . import Expense
class BudgetList():
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overage = []

    def append(self, item):
        if self.sum_expenses + item < self.budget:
            self.expenses.append(item)
            self.sum_expenses =self.sum_expenses + item
        else:
            self.overage.append(item)
            self.sum_overages + self.sum_overages+item

    def __len__(self):
         return self.expenses + self.overage

def main():
        myBudgetList = BudgetList(1200)
        expenses =Expense.Expenses()
        expenses.read_expenses('data/spending_data.csv')
        for expense  in expenses.list:
            myBudgetList.append(expense.amount)
        print('The count of all expenses: ' + str(len(myBudgetList.__len__())))


if __name__ == "__main__":
    main()
