from unittest import TestCase
from challenges.bank_account import BankAccount


class TestBank(TestCase):
    def test_deposit(self):
        user = BankAccount("Amit")
        user.deposit(100)
        self.assertEqual(user.bal, 100)

        user = BankAccount("Amit")
        user.deposit(-100)
        self.assertEqual(user.bal, 0)

        user = BankAccount("Amit", 200)
        user.deposit(-100)
        self.assertEqual(user.bal, 200)

        user = BankAccount("Amit")
        user.deposit(0)
        self.assertEqual(user.bal, 0)

        user = BankAccount("Amit", 100)
        user.deposit(0)
        self.assertEqual(user.bal, 100)

    def test_withdraw(self):
        user = BankAccount("Amit")
        user.withdraw(100)
        self.assertEqual(user.bal, 0)

        user = BankAccount("Amit", 200)
        user.withdraw(100)
        self.assertEqual(user.bal, 100)

        user = BankAccount("Amit", 100)
        user.withdraw(200)
        self.assertEqual(user.bal, 100)

        user = BankAccount("Amit", 200)
        user.withdraw(200)
        self.assertEqual(user.bal, 0)

        user = BankAccount("Amit", 100)
        user.withdraw(-100)
        self.assertEqual(user.bal, 100)

