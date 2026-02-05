class Expense:
    def __init__(self, amount, category, date, description):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def __str__(self):
        return f"Date: {self.date}, Category: {self.category}, Amount: {self.amount}, Description: {self.description}"