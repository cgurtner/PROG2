import secrets # this needs python 3.6+

class BankAccount:
    def __init__(self, isOpen = True, balance = 0, currency = 'CHF'):
        # this simulates the IBAN.
        self.iban = secrets.token_hex(16).upper()
        self.isOpen = isOpen
        self.balance = balance
        self.currecy = currency

    def getIBAN(self) -> str:
        return self.iban

    def getIsOpen(self) -> bool:
        return self.isOpen

    def setIsOpen(self, newIsOpen) -> None:
        self.isOpen = newIsOpen
    
    def getBalance(self) -> int:
        return self.balance

    def getCurrency(self) -> str:
        return self.currecy

    def printBalance(self) -> None:
        print('The balance of account ' + self.iban + ' is ' + str(self.balance) + self.currecy + '.')
    
    def deposit(self, amount) -> None:
        # this should be changed with proper exception handling
        if not self.isOpen:
            print('This account is closed!')
        elif self.balance + amount > 100000:
            print('This would exceed the limit.')
        else:
            self.balance += amount

    def withdraw(self, amount) -> None:
        # this should be changed with proper exception handling
        if not self.isOpen:
            print('This account is closed!')
        elif self.balance - amount < 0:
            print('You can\'t withdraw that amount!')
        else:
            self.balance -= amount

# this code is only ran if invoced directly e.g. python3 BankAccount.py
# it is prevented from being run if imported into other file
if __name__ == '__main__':
    acc = BankAccount()
    print('Test ' + acc.getIBAN())
    acc.deposit(50000)
    acc.printBalance()
    acc.withdraw(2)
    acc.printBalance()
    print('\n')

    acc2 = BankAccount()
    print('Test ' + acc2.getIBAN())
    acc2.deposit(90000)
    acc2.printBalance()
    acc2.withdraw(91000)
    acc2.printBalance()
    print('\n')

    acc3 = BankAccount()
    print('Test ' + acc3.getIBAN())
    acc3.deposit(105000)
    acc3.printBalance()
    print('\n')

    acc4 = BankAccount()
    print('Test ' + acc4.getIBAN())
    acc4.deposit(50000)
    acc4.printBalance()
    acc4.setIsOpen(False)
    acc4.withdraw(10000)
    acc4.printBalance()