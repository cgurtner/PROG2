from Client import Client
from BankAccount import BankAccount
from SavingAccount import SavingAccount
from YouthAccount import YouthAccount

class BankApplication:
    def __init__(self) -> None:
        self.client = None
        self.accounts = {}
        self.current_account = None

    def get_client(self) -> Client:
        return self.client

    def get_accounts(self) -> dict:
        return self.accounts

    def has_accounts(self) -> bool:
        return len(self.get_accounts()) > 0

    def add_account(self, account: BankAccount) -> None:
        self.accounts[account.get_iban()] = account
    
    def run(self):
        while True:
            if not self.client:
                print('###### Bank of Pythonia ###### ')
                print('You are not a client yet. To access your E-Banking menu please give us some information:')
                self.client = self.open_client()
            if not self.has_accounts():
                print('You have no accounts yet, please open one:')
                self.add_account(self.open_account())

    def open_client(self) -> Client:
        first_name = input('Your first name: ')
        name = input('Your last name: ')
        address = input('Please give us your address: ')
        birthday = input('Your date of birth in the format YYYY-MM-DD: ')
        return Client(first_name, name, address, birthday)

    def open_account(self) -> BankAccount:
        created_account = False
        # this explizit bool()-cast is needed because it trigger the __bool__ magic inside YouthAccount
        while bool(created_account) == False:
            choice = int(input('Do you want to open a [1] SavingsAccount or [2] YouthAccount? '))
            if choice == 1:
                created_account = SavingAccount(self.get_client())
            elif choice == 2:
                created_account = YouthAccount(self.get_client())
        return created_account

if __name__ == '__main__':
    app = BankApplication()
    app.run()
