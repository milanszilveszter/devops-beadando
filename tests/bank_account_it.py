import unittest
from bank import bank_account

class TestBankAccountIntegration(unittest.TestCase):
    def test_transaction_flow(self):
        account = bank_account("Elek Víz", 200)
        account.deposit(100)
        account.withdraw(50)

        self.assertEqual(account.get_balance(), 250)

if __name__ == "__main__":
    unittest.main()