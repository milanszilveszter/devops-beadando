import pytest
import bank_account

@pytest.fixture
def account():
    return bank_account("Árpi Nagy", 100)

def test_deposit(account):
    assert account.deposit(50) == 150
    with pytest.raises(ValueError, match="Deposit amount must be positive."):
        account.deposit(-10)

def test_withdraw(account):
    assert account.withdraw(30) == 70
    with pytest.raises(ValueError, match="Withdrawal amount must be positive."):
        account.withdraw(-10)
    with pytest.raises(ValueError, match="Insufficient funds."):
        account.withdraw(200)

def test_get_balance(account):
    assert account.get_balance() == 100