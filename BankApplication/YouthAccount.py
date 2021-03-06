from datetime import datetime
from BankAccount import BankAccount
from Client import Client

class YouthAccount(BankAccount):
    def __init__(self, client: Client, is_open=True, balance=0, currency='CHF'):
        # value of monthly_interest can only be changed here (programmatically)
        super().__init__(client, is_open, balance, currency, 0.02)
        
        # set is_open=False if on creation time the client is too old
        if client.get_age() > 25:
            self.set_is_open(False)
    
    def __str__(self):
        ret = '** YoungAccount ' + self.get_iban() + ' ** '
        ret += self.get_formatted_balance() + ' ' + self.get_currency()
        return ret
    
    # we use this magic function with is_open() as bool representation
    # this also allows us to use Client object in conditionals directly
    def __bool__(self):
        return self.get_is_open()

    # Overrides super().withdraw()
    def withdraw(self, amount) -> None:
        if self.withdraw_allowed(amount):
            super().withdraw(amount)
        else:
            print('You can\'t withdraw that amount this month!')
    
    def withdraw_allowed(self, amount) -> bool:
        date = datetime.now()
        date_string = str(date.year) + '-' + str(date.month)
        move = self.get_movement()
        if date_string in move['withdraw']:
            if move['withdraw'][date_string] + amount > 2000:
                return False
        elif amount > 2000:
            return False
        return True

if __name__ == '__main__':
    c = Client('First', 'Last', 'Address', '1992-07-20')

    acc = YouthAccount(c)
    if not acc: print('Account was not opened!\n')

    c = Client('First', 'Last', 'Address', '2000-07-20')
    acc = YouthAccount(c)
    print('Test ' + acc.get_iban())
    acc.deposit(5000)
    acc.print_balance()
    acc.withdraw(500)
    acc.print_balance()
    print('\n')

    acc = YouthAccount(c)
    print('Test ' + acc.get_iban())
    acc.deposit(5000)
    acc.withdraw(3500)
    acc.print_balance()
    print('\n')

    acc = YouthAccount(c)
    print('Test ' + acc.get_iban())
    acc.deposit(5000)
    acc.withdraw(200)
    acc.withdraw(300)
    acc.withdraw(500)
    acc.withdraw(1001)
    acc.print_balance()
    print('\n')
    