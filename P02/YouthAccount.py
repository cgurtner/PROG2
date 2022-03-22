from BankAccount import BankAccount

class YouthAccount(BankAccount):
    def __init__(self, is_open=True, balance=0, currency='CHF'):
        super().__init__(is_open, balance, currency)

        # this attribute is private and has no setter-method
        # to ensure it can be only changed here programmatically
        self.__monthly_interest = 0.02

    # Overrides super().withdraw()
    def withdraw(self, amount) -> None:
        super().withdraw(amount)