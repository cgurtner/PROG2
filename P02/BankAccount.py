import secrets # this needs python 3.6+
from Client import Client

class BankAccount:
    def __init__(self, client: Client, is_open=True, balance=0, currency='CHF'):
        # this is the owner of the account
        self.client = client
        # this simulates the IBAN.
        self.iban = secrets.token_hex(2).upper()
        self.is_open = is_open
        self.balance = balance
        self.currecy = currency

    def __str__(self):
        ret = 'Account ' + self.get_iban() + ' is '
        if self.get_is_open():
            ret += 'open '
        else:
            ret += 'closed '
        ret += 'and has ' + str(self.get_balance()) + ' ' + self.get_currency() + ' stored in it.'
        return ret

    def get_iban(self) -> str:
        return self.iban

    def get_is_open(self) -> bool:
        return self.is_open

    def set_is_open(self, new_is_open) -> None:
        self.is_open = new_is_open
    
    def get_balance(self) -> int:
        return self.balance

    def get_currency(self) -> str:
        return self.currecy

    def open(self) -> None:
        self.set_is_open(True)

    def close(self) -> None:
        self.set_is_open(False)
    
    def deposit(self, amount) -> None:
        # this should be changed with proper exception handling
        if not self.is_open:
            print('This account is closed!')
        elif self.balance + amount > 100000:
            print('This would exceed the limit.')
        else:
            self.balance += amount

    def withdraw(self, amount) -> None:
        # this should be changed with proper exception handling
        if not self.is_open:
            print('This account is closed!')
        elif self.balance - amount < 0:
            print('You can\'t withdraw that amount!')
        else:
            self.balance -= amount

    def print_balance(self) -> None:
        print('The balance of account ' + self.iban + ' is ' + str(self.balance) + self.currecy + '.')

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