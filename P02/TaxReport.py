class TaxReport:
    def __init__(self, app):
        self.app = app

    def generate(self):
        account_list = self.app.get_accounts()
        for key, acc in account_list.items():
            print(acc)
