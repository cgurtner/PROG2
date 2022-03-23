from BankAccount import BankAccount
from Client import Client

class SavingAccount(BankAccount):
    WITHDRAW_COMMISSION = 0.02

    def __init__(self, client: Client, is_open=True, balance=0, currency='CHF', monthly_interest=0.001):
        super().__init__(client, is_open, balance, currency)
        self.monthly_interest = monthly_interest

    def set_monthly_interest(self, mi) -> None:
        self.monthly_interest = mi

    # Overrides super().withdraw()
    def withdraw(self, amount) -> None:
        if not self.is_open:
            print('This account is closed!')
        elif self.balance - amount < 0:
            amount += amount * SavingAccount.WITHDRAW_COMMISSION
        self.balance -= amount