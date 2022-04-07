from Provider.ExchangeRateProvider import ExchangeRateProvider

class TaxReport:
    TAX_REPORT_CURRENCY = 'CHF'

    def __init__(self, app):
        self.app = app
        self.api = ExchangeRateProvider()

    def generate(self):
        print('\n###### Tax-Report ######\n')
        account_list = self.app.get_accounts()
        for key, acc in account_list.items():
            s = '** ' + acc.__class__.__name__ + ' ' + acc.get_iban() + ' ** '
            if acc.get_currency() == TaxReport.TAX_REPORT_CURRENCY:
                s += format(acc.get_balance(), '.2f') + ' ' + acc.get_currency()
            else:
                self.api.set_base_code(acc.get_currency())
                self.api.set_target_code(TaxReport.TAX_REPORT_CURRENCY)
                self.api.conversion(acc.get_balance())
                s += format(self.api.get_conversion_result(), '.2f') + ' ' + self.api.get_target_code() + ' '
                s += '(base: ' + self.api.get_base_code() + ', rate: ' + str(self.api.get_conversion_rate()) + ')'
            print(s)