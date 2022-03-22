from BankAccount import BankAccount
from Client import Client

class YouthAccount(BankAccount):
    def __init__(self, client: Client, is_open=True, balance=0, currency='CHF'):
        super().__init__(client, is_open, balance, currency)

        # this attribute is private and has no setter-method
        # to ensure it can be only changed here programmatically
        self.__monthly_interest = 0.02
        
        # set is_open=False if on creation time the client is too old
        if client.get_age() > 25:
            self.set_is_open(False)
    
    # we use this magic function with is_open() as bool representation
    # this also allows us to use Client object in conditionals directly
    def __bool__(self):
        return self.get_is_open()

    # Overrides super().withdraw()
    def withdraw(self, amount) -> None:
        super().withdraw(amount)