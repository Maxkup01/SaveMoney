from datetime import datetime
class Money:
    def __init__(
        self, 
        id :int, 
        income: int, 
        expenses: int, 
        date: datetime, 
        note: str):
     self.id = id
     self.income = income
     self.expenses = expenses
     self.date = date
     self.note = note
    def __repr__(self):
       return f'<Money: {self.id}>'