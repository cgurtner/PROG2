from Provider.ExchangeRateProvider import ExchangeRateProvider

class TaxReport:
    TAX_REPORT_CURRENCY = 'CHF'

    def __init__(self, app):
        self.app = app
        self.api = ExchangeRateProvider()

    def generate(self):
        print('\n###### Tax-Report ######\n')
        account_list = self.app.get_accounts()
        total_tax = 0
        s = ''
        for key, acc in account_list.items():
            s += '** ' + acc.__class__.__name__ + ' ' + acc.get_iban() + ' ** '
            if acc.get_currency() == TaxReport.TAX_REPORT_CURRENCY:
                s += acc.get_formatted_balance() + ' ' + acc.get_currency() + '\n'
            else:
                self.api.set_base_code(acc.get_currency())
                self.api.set_target_code(TaxReport.TAX_REPORT_CURRENCY)
                self.api.conversion(acc.get_balance())
                total_tax += self.api.get_conversion_result()
                s += self.api.get_formatted_conversion_result() + ' ' + self.api.get_target_code() + ' '
                s += '(' + acc.get_formatted_balance() + ' ' + acc.get_currency() + ' '
                s += '[exchange-rate: ' + str(self.api.get_conversion_rate()) + ']) \n'
        s += '\n Total Tax: ' + format(total_tax, '.2f') + ' ' + TaxReport.TAX_REPORT_CURRENCY
        print(s)