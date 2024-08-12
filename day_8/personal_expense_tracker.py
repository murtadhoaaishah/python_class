# personal expense tracker
import csv


# usecase 1: check when spending beyond budget
# usecase 2: check where most money goes
# usecase 3: calculate / group essential and non essential needs

# requirements
# amount at hand
# category of needs
# income
# expenditure
# amount left
# amount to spend
# amount to save
# time 
# day we spend most

class Expense:

    expense_file = "expense.csv"
    categories = ['food','cosmetics', 'toiletries', 'wears', 'others']

    def _init_(self):
        self.amount = 0
        self.budget = 0
        self.income = 0
    
    def make_budget(self,current_income, percentage):
        self.budget = (percentage / 100) * current_income
        self.income = current_income

    def create_new_expense(self, category_num, amount, description):
        # User should be able to select category based on the category list shown abovw
        if category_num == 1:
            category = Expense.categories[0]
        elif category_num == 2:
                category = Expense.categories[1]
        elif category_num == 3:
                category = Expense.categories[2]
        elif category_num == 4:
             category = Expense.categories[3]
        elif category_num == 5:
             category = Expense.categories[4]
        else:
                print("Invalid category choice")

        # category = input("Enter category name: ").lower()
# create a new header if header is not present
        if self.budget >= amount:
            self.budget -= amount
            self.amount = amount
            header = ['description', 'amount', 'category', 'balance']
            with open(Expense.expense_file, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerow([description, self.amount, category, self.budget])
            print(f"you have successfully purchased, {description} and your balance is {self.budget}")
        else:
            print("Insufficient balance")

income = int(input('Enter your current income:'))
percentage  = int(input('Enter your current percentage:'))
amount = int(input('Enter amount: '))
description = input('Enter description: ')

new_expense = Expense()
new_expense.make_budget(income, percentage)
print(f'1.food\n2. cosmetics\n3. toiletries\n4. wears\n5. others')
category_num = int(input('category: '))
new_expense.create_new_expense(category_num, amount, description)
