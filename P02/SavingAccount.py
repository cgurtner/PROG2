from BankAccount import BankAccount

class SavingAccount(BankAccount):
    def __init__(self, is_open=True, balance=0, currency='CHF', monthly_interest=0.001):
        super().__init__(is_open, balance, currency)
        self.monthly_interest = monthly_interest

    def withdraw(self, amount) -> None:
        if not self.is_open:
            print('this account is closed')
        elif self.balance - amount < 0:
            amount += amount * 0.02
        self.balance -= amount