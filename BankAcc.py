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
        if self.bal < amount:
            return False
        else:
            if amount > -0:
                self.bal -= amount
                return True

            return False


if __name__ == '__main__':
    BankAccount("Kiran")
    amit = BankAccount("Amit")
    bacchan = BankAccount("Bacchan", 500)
    bacchan.withdraw(600)
    amit.withdraw(200)
    amit.deposit(150)
    amit.withdraw(200)
    amit.deposit(-10)