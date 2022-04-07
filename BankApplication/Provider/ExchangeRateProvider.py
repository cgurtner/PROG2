import json
import requests

# this class uses https://www.exchangerate-api.com to calculcate exchange rates from, to currency
# it was found on https://www.programmableweb.com/api/exchange-rate
# ExchangeRate-API has a limit of 1500 monthly requests in it's free-to-use version

# I evaluated other APIs but stumbled on various problems. 
# Most of them didn't allow conversion from base USD in their free version.
# I will delete my API_KEY after this assignment is graded.

class ExchangeRateProvider:
    API_KEY = 'fe98d52412a187a896fccf11'
    API_CONVERSION_URL = 'https://v6.exchangerate-api.com/v6/' + API_KEY + '/pair/{base}/{target}/{amount}'
    API_CURRENCY_URL = 'https://v6.exchangerate-api.com/v6/' + API_KEY + '/latest/CHF'

    def __init__(self) -> None:
        self.base_code = None
        self.target_code = None
        self.conversion_rate = None
        self.conversion_result = None
    
    def set_base_code(self, code) -> None:
        self.base_code = code

    def get_base_code(self) -> str:
        return self.base_code

    def set_target_code(self, code) -> None:
        self.target_code = code

    def get_target_code(self) -> str:
        return self.target_code

    def get_conversion_rate(self) -> float:
        return self.conversion_rate

    def get_conversion_result(self) -> float:
        return self.conversion_result

    def get_formatted_conversion_result(self) -> str:
        return format(self.get_conversion_result(), '.2f')

    def get_url_conversion_rates(self):
        return ExchangeRateProvider.API_CURRENCY_URL
    
    def get_url_conversion(self, amount):
        base = self.get_base_code()
        target = self.get_target_code()
        return ExchangeRateProvider.API_CONVERSION_URL.format(base=base, target=target, amount=amount)

    def fetch_conversion_rates(self):
        return self.__fetch(self.get_url_conversion_rates())['conversion_rates']
    
    def fetch_conversion(self, amount):
        return self.__fetch(self.get_url_conversion(amount))

    def validate(self) -> bool:
        if self.get_target_code() == None:
            raise Exception('no target_code is set!')
        if self.get_base_code() == None:
            raise Exception(' no base_code is set!')
        
        # I'm fetching the conversion rates to verify that conversion is possible
        # For the sake of this assignment I'm only fetching the possible conversion rates for CHF
        conversion_rates = self.fetch_conversion_rates()
        if self.get_base_code() not in conversion_rates:
            raise Exception('conversion from base ' + self.get_base_code() + ' not possible!')
        if self.get_target_code() not in conversion_rates:
            raise Exception('conversion into target ' + self.get_target_code() + ' not possible!')

    def conversion(self, amount: float) -> json:
        self.validate()
        resp = self.fetch_conversion(amount)
        self.base_code = resp['base_code']
        self.target_code = resp['target_code']
        self.conversion_rate = float(resp['conversion_rate'])
        self.conversion_result = float(resp['conversion_result'])

    # this method is private because only wrapper methods should use this
    # e.g. fetch_conversion()
    def __fetch(self, url) -> json:
        return requests.get(url).json()

if __name__ == '__main__':
    print('###### Bank of Pythonia: ExchangeRateConversion ######\n')
    while True:
        base = input('Currency to convert from: ')
        target = input('Currency to convert to: ')

        api = ExchangeRateProvider()
        api.set_base_code(base)
        api.set_target_code(target)

        print('\n#### You are calculating the conversion result from {base} to {target} ####\n'.format(base=api.get_base_code(), target=api.get_target_code()))
        amount = float(input('Amount to exchange: '))
        api.conversion(amount)

        output = '\nConversion of {base_amount} {base_code} gives you {conversion_result} {target_code} (rate: {conversion_rate})\n'
        print(output.format(base_amount=format(amount, '.2f'), base_code=api.get_base_code(), conversion_result=api.get_formatted_conversion_result(), target_code=api.get_target_code(), conversion_rate=api.get_conversion_rate()))
