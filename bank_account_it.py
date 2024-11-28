import pytest
import bank_account


def test_transaction_flow():
    account = bank_account("Jane Smith", 200)
    account.deposit(100) 
    account.withdraw(50) 
     
    assert account.get_balance() == 250