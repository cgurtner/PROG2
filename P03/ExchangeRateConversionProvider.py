import json
import requests

# this class uses https://www.exchangerate-api.com to calculcate exchange rates from, to currency
# it was found on https://www.programmableweb.com/api/exchange-rate
# ExchangeRate-API has a limit of 1500 monthly requests in it's free-to-use version

# I evaluated other APIs but stumbled on various problems. 
# Most of them didn't allow conversion from base USD in their free version.
# I will delete my API_KEY after this assignment is graded.

class ExchangeRateConversionProvider:
    API_URL = 'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{base}/{to}/'
    API_KEY = 'fe98d52412a187a896fccf11'

    def __init__(self, params: dict) -> None:
        self.base_code = None
        self.target_code = None
        self.conversion_rate = None
        self.conversion_result = None

        if 'base' not in params:
            raise Exception('no {base} parameter is set!')
        if 'to' not in params:
            raise Exception('no {to} parameter is set!')
        
        self.url = ExchangeRateConversionProvider.API_URL.format(API_KEY=ExchangeRateConversionProvider.API_KEY, base=params['base'], to=params['to'])

    def fetch_from_amount(self, amount: float) -> json:
        resp = self.__fetch(self.url + str(amount))
        self.base_code = resp['base_code']
        self.target_code = resp['target_code']
        self.conversion_rate = float(resp['conversion_rate'])
        self.conversion_result = float(resp['conversion_result'])

    def get_base_code(self) -> str:
        return self.base_code

    def get_target_code(self) -> str:
        return self.target_code

    def get_conversion_rate(self) -> float:
        return self.conversion_rate
    
    def get_conversion_result(self) -> float:
        return self.conversion_result

    def get_formatted_conversion_result(self) -> str:
        return format(self.get_conversion_result(), '.2f')

    # this method is private because only wrapper methods should use this
    # e.g. get_value_from_amount()
    def __fetch(self, url) -> json:
        response = requests.get(url)
        return response.json()

if __name__ == '__main__':
    print('###### Bank of Pythonia: ExchangeRateConversion ######\n')
    while True:
        base = input('Currency to convert from: ')
        to = input('Currency to convert to: ')
        api = ExchangeRateConversionProvider({'base': base, 'to': to})

        print('\n#### You are calculating the conversion result from {base} to {to} ####\n'.format(base=base, to=to))
        amount = float(input('Amount to exchange: '))
        api.fetch_from_amount(amount)

        output = '\nConversion of {base_amount} {base_code} gives you {conversion_result} {target_code} (rate: {conversion_rate})\n'
        print(output.format(base_amount=format(amount, '.2f'), base_code=api.get_base_code(), conversion_result=api.get_formatted_conversion_result(), target_code=api.get_target_code(), conversion_rate=api.get_conversion_rate()))
