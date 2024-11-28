import unittest
from bank import bank_account

class TestBankAccountUnit(unittest.TestCase):
    def setUp(self):
        self.account = bank_account("Árpi Nagy", 100)

    def test_deposit(self):
        self.assertEqual(self.account.deposit(50), 150)
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    def test_withdraw(self):
        self.assertEqual(self.account.withdraw(30), 70)
        with self.assertRaises(ValueError):
            self.account.withdraw(-10)
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 100)

if __name__ == "__main__":
    unittest.main()