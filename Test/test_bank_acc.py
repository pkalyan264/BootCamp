import unittest
from Challenges import bank_account


class TestBank(unittest.TestCase):
    def test_user_initialisation(self):
        user = bank_account.BankAccount("Amit")
        self.assertEqual(user.owner, "Amit")
        self.assertEqual(user.bal, 0)

        user = bank_account.BankAccount("Amit", 10)
        self.assertEqual(user.owner, "Amit")
        self.assertEqual(user.bal, 10)

        user = bank_account.BankAccount("Kiran", -5)
        self.assertEqual(user.owner, "Kiran")
        self.assertEqual(user.bal, 0)

        user = bank_account.BankAccount("123435")
        self.assertEqual(user.owner, "123435")
        self.assertEqual(user.bal, 0)

    def test_deposit_func(self):
        user = bank_account.BankAccount("Amit")
        user.deposit(100)
        self.assertEqual(user.bal, 100)

        user = bank_account.BankAccount("Amit")
        user.deposit(-100)
        self.assertEqual(user.bal, 0)

        user = bank_account.BankAccount("Amit", 200)
        user.deposit(-100)
        self.assertEqual(user.bal, 200)

        user = bank_account.BankAccount("Amit")
        user.deposit(0)
        self.assertEqual(user.bal, 0)

        user = bank_account.BankAccount("Amit", 100)
        user.deposit(0)
        self.assertEqual(user.bal, 100)

    def test_withdraw_func(self):
        user = bank_account.BankAccount("Amit")
        user.withdraw(100)
        self.assertEqual(user.bal, 0)

        user = bank_account.BankAccount("Amit", 200)
        user.withdraw(100)
        self.assertEqual(user.bal, 100)

        user = bank_account.BankAccount("Amit", 100)
        user.withdraw(200)
        self.assertEqual(user.bal, 100)

        user = bank_account.BankAccount("Amit", 200)
        user.withdraw(200)
        self.assertEqual(user.bal, 0)

        user = bank_account.BankAccount("Amit", 100)
        user.withdraw(-100)
        self.assertEqual(user.bal, 100)

