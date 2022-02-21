class BankAccount:
    def __init__(self, owner, bal=0):
        self.owner = owner
        if bal >= 0:
            self.bal = bal
        else:
            self.bal = 0

    def deposit(self, amount):
        if amount <= 0:
            return False
        else:
            self.bal += amount
            return True

    def withdraw(self, amount):
        if 0 <= amount <= self.bal:
            self.bal -= amount
            return True

        return False

