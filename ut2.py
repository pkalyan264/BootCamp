import unittest
import BankAcc


class TestBank(unittest.TestCase):
    def test_user_initialisation(self):
        user = BankAcc.BankAccount("Amit")
        self.assertEqual(user.owner, "Amit")
        self.assertEqual(user.bal, 0)

        user = BankAcc.BankAccount("Amit", 10)
        self.assertEqual(user.owner, "Amit")
        self.assertEqual(user.bal, 10)

        user = BankAcc.BankAccount("Kiran", -5)
        self.assertEqual(user.owner, "Kiran")
        self.assertEqual(user.bal, 0)

        user = BankAcc.BankAccount("123435")
        self.assertEqual(user.owner, "123435")
        self.assertEqual(user.bal, 0)

    def test_deposit_func(self):
        user = BankAcc.BankAccount("Amit")
        user.deposit(100)
        self.assertEqual(user.bal, 100)

        user = BankAcc.BankAccount("Amit")
        user.deposit(-100)
        self.assertEqual(user.bal, 0)

        user = BankAcc.BankAccount("Amit", 200)
        user.deposit(-100)
        self.assertEqual(user.bal, 200)

        user = BankAcc.BankAccount("Amit")
        user.deposit(0)
        self.assertEqual(user.bal, 0)

        user = BankAcc.BankAccount("Amit", 100)
        user.deposit(0)
        self.assertEqual(user.bal, 100)

    def test_withdraw_func(self):
        user = BankAcc.BankAccount("Amit")
        user.withdraw(100)
        self.assertEqual(user.bal, 0)

        user = BankAcc.BankAccount("Amit", 200)
        user.withdraw(100)
        self.assertEqual(user.bal, 100)

        user = BankAcc.BankAccount("Amit", 100)
        user.withdraw(200)
        self.assertEqual(user.bal, 100)

        user = BankAcc.BankAccount("Amit", 200)
        user.withdraw(200)
        self.assertEqual(user.bal, 0)

        user = BankAcc.BankAccount("Amit", 100)
        user.withdraw(-100)
        self.assertEqual(user.bal, 100)

#
# if __name__ == '__main__':
#     test_user_initialisation()
#     unittest.main()
#     test_user_initialisation()
