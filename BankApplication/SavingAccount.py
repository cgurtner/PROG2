from BankAccount import BankAccount
from Client import Client

class SavingAccount(BankAccount):
    WITHDRAW_COMMISSION = 0.02

    def __init__(self, client: Client, is_open=True, balance=0, currency='CHF', monthly_interest=0.001):
        super().__init__(client, is_open, balance, currency, monthly_interest)

    def __str__(self):
        ret = '** SavingAccount ' + self.get_iban() + ' ** '
        ret += self.get_formatted_balance() + ' ' + self.get_currency()
        return ret

    def set_monthly_interest(self, mi) -> None:
        self.monthly_interest = mi

    # Overrides super().withdraw()
    def withdraw(self, amount) -> None:
        amount_to_withdraw = amount
        if not self.is_open:
            print('This account is closed!')
        elif self.balance - amount < 0:
            amount_to_withdraw = amount_to_withdraw + amount_to_withdraw * SavingAccount.WITHDRAW_COMMISSION
        self.balance -= amount_to_withdraw
        self.add_movement('withdraw', amount_to_withdraw)

if __name__ == '__main__':
    c = Client('First', 'Last', 26, '1992-07-20')

    acc = SavingAccount(c)
    print('Test ' + acc.get_iban())
    acc.deposit(50000)
    acc.print_balance()
    acc.withdraw(2)
    acc.print_balance()
    print('\n')

    acc = SavingAccount(c)
    print('Test ' + acc.get_iban())
    print('WITHDRAW_COMMISSION = ' + str(SavingAccount.WITHDRAW_COMMISSION))
    acc.deposit(50000)
    acc.print_balance()
    acc.withdraw(60000)
    acc.print_balance()
    print('\n')

    acc = SavingAccount(c)
    print('Test ' + acc.get_iban())
    acc.close()
    acc.deposit(50000)
    print('\n')