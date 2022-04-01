from Client import Client
from BankAccount import BankAccount
from SavingAccount import SavingAccount
from YouthAccount import YouthAccount
from TaxReport import TaxReport

class BankApplication:
    def __init__(self) -> None:
        self.client = None
        self.accounts = {}
        self.current_account = None

    def get_client(self) -> Client:
        return self.client

    def get_accounts(self) -> dict:
        return self.accounts

    def get_current_account(self) -> BankAccount:
        return self.current_account

    def has_accounts(self) -> bool:
        return len(self.get_accounts()) > 0

    def add_account(self, account: BankAccount) -> None:
        self.accounts[account.get_iban()] = account
    
    def run(self):
        while True:
            if not self.client:
                print('###### Bank of Pythonia ######\n')
                print('You are not a client yet.\nTo access your E-Banking menu please give us some information:\n')
                self.client = self.create_client()
            elif not self.has_accounts():
                print('\nYou have no accounts yet, please open one:')
                self.add_account(self.create_account())
            elif self.get_current_account():
                self.menu_account()
            else:
                print('\n###### Main Menu ######\n')
                print('[1] Create additional account')
                print('[2] Choose account')
                print('[3] Print Tax-Report\n')
                choice = int(input('Type [1], [2] or [3]: '))
                if choice == 1:
                    self.add_account(self.create_account())
                elif choice == 2:
                    self.current_account = self.choose_account_to_interact_with()
                elif choice == 3:
                    tax_report = TaxReport(self)
                    tax_report.generate()


    def create_client(self) -> Client:
        first_name = input('Your first name: ')
        name = input('Your last name: ')
        address = input('Please give us your address: ')
        birthday = input('Your date of birth in the format YYYY-MM-DD: ')
        return Client(first_name, name, address, birthday)

    def create_account(self) -> BankAccount:
        created_account = False
        # this explizit bool()-cast is needed because it triggers the __bool__ magic inside YouthAccount
        while bool(created_account) == False:
            choice = int(input('\nDo you want to open a [1] SavingsAccount or [2] YouthAccount? '))
            if choice == 1:
                created_account = SavingAccount(self.get_client())
            elif choice == 2:
                created_account = YouthAccount(self.get_client())
                if not created_account: print('Not possible, you are too old!')
        return created_account

    def choose_account_to_interact_with(self) -> BankAccount:
        print('\n###### Account List ######\n')
        for key, obj in self.get_accounts().items():
            print(obj)
        iban = input('\nType in the IBAN you wanna interact with: ')
        if iban in self.get_accounts():
            return self.get_accounts()[iban]
        else:
            return self.choose_account_to_interact_with()

    def menu_account(self) -> None:
        print('\n###### Account Menu ######\n')
        print(self.get_current_account())
        print('\n[1] deposit')
        print('[2] withdraw')
        print('[3] close')
        print('[4] back to main menu\n')
        action = int(input('Type the number of you choice: '))
        if action == 1:
            amount = float(input('What amount do you wanna deposit: '))
            self.get_current_account().deposit(amount)
        elif action == 2:
            amount = float(input('What amount do you wanna withdraw: '))
            self.get_current_account().withdraw(amount)
        elif action == 3:
            self.get_current_account().close()
            del self.accounts[self.get_current_account().get_iban()]
            self.current_account = None
        elif action == 4:
            self.current_account = None

if __name__ == '__main__':
    app = BankApplication()
    app.run()
