from Client import Client
from SavingAccount import SavingAccount
from YouthAccount import YouthAccount

class BankApplication:
    def __init__(self) -> None:
        self.accounts = {}
        self.client = None
        self.current_account = None
    
    def has_accounts(self):
        return len(self.accounts) > 0
    
    def run(self):
        while True:
            if not self.client:
                print('###### Bank of Pythonia ###### ')
                print('You are not a client yet. To access your E-Banking menu please give us some information:')

                first_name = input('Your first name: ')
                name = input('Your last name: ')
                address = input('Please give us your address:')
                birthday = input('Your date of birth in the format YYYY-MM-DD:')

                self.client = Client(first_name, name, address, birthday)

if __name__ == '__main__':
    app = BankApplication()
    app.run()
