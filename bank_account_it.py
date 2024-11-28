import pytest
from bank_account import BankAccount



def test_transaction_flow():
    account = BankAccount("Jane Smith", 200)
    account.deposit(100) 
    account.withdraw(50) 
     
    assert account.get_balance() == 250