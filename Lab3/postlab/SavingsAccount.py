class SavingsAccount:

    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __lt__(self, other):
        return self.name < other.name

    def __eq__(self, other):
        return self.name == other.name

    def __ge__(self, other):
        return self.name >= other.name

    def __str__(self):
        return f"Account(Name: {self.name}, Balance: ${self.balance:.2f})"
