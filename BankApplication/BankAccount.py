import secrets # this needs python 3.6+
from datetime import datetime
from Client import Client

class BankAccount:
    def __init__(self, client: Client, is_open=True, balance=0, currency='CHF', monthly_interest=0):
        # this is the owner of the account
        self.client = client
        # this simulates the IBAN.
        self.iban = secrets.token_hex(2).upper()
        self.is_open = is_open
        self.balance = balance
        self.currency = currency
        self.monthly_interest = monthly_interest
        self.movement = {'deposit': {}, 'withdraw': {}}

    def __str__(self):
        ret = '** BankAccount ' + self.get_iban() + ' ** '
        ret += self.get_formatted_balance() + ' ' + self.get_currency()
        return ret

    def get_iban(self) -> str:
        return self.iban

    def get_is_open(self) -> bool:
        return self.is_open

    def set_is_open(self, new_is_open) -> None:
        self.is_open = new_is_open
    
    def get_balance(self) -> int:
        return self.balance

    def get_formatted_balance(self) -> str:
        return format(self.balance, '.2f')

    def get_currency(self) -> str:
        return self.currency

    def set_currency(self, curr) -> None:
        self.currency = curr

    def add_monthly_interest(self) -> None: 
        self.balance += self.balance * self.monthly_interest

    def add_movement(self, type, amount):
        date = datetime.now()
        date_string = str(date.year) + '-' + str(date.month)
        if date_string in self.movement[type]:
            self.movement[type][date_string] += amount
        else:
            self.movement[type][date_string] = amount

    def get_movement(self) -> dict: 
        return self.movement

    def open(self) -> None:
        self.set_is_open(True)

    def close(self) -> None:
        self.set_is_open(False)
    
    def deposit(self, amount) -> None:
        # this should be changed with proper exception handling
        if not self.get_is_open():
            print('This account does not exist anymore!')
        elif self.get_balance() + amount > 100000:
            print('This would exceed the limit.')
        else:
            self.balance += amount
            self.add_movement('deposit', amount)

    def withdraw(self, amount) -> None:
        # this should be changed with proper exception handling
        if self.balance - amount < 0:
            print('You don\'t have enough money!')
        else:
            self.balance -= amount
            self.add_movement('withdraw', amount)

    def print_balance(self) -> None:
        print('The balance of account ' + self.iban + ' is ' + str(self.balance) + self.currency + '.')

# this code is only ran if invoced directly e.g. python3 BankAccount.py
# it is prevented from being run if imported into other file
if __name__ == '__main__':
    acc = BankAccount()
    print('Test ' + acc.get_iban())
    acc.deposit(50000)
    acc.print_balance()
    acc.withdraw(2)
    acc.print_balance()
    print('\n')

    acc2 = BankAccount()
    print('Test ' + acc2.get_iban())
    acc2.deposit(90000)
    acc2.print_balance()
    acc2.withdraw(91000)
    acc2.print_balance()
    print('\n')

    acc3 = BankAccount()
    print('Test ' + acc3.get_iban())
    acc3.deposit(105000)
    acc3.print_balance()
    print('\n')

    acc4 = BankAccount()
    print('Test ' + acc4.get_iban())
    acc4.deposit(50000)
    acc4.print_balance()
    acc4.close()
    acc4.withdraw(10000)
    acc4.print_balance()