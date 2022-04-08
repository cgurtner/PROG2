from time import sleep
import pandas as pd
import requests

class BillOfMaterialsProvider:
    API_URL = 'http://160.85.252.148'
    BACKOFF_FACTOR = 1

    def __init__(self):
        data = self.fetch()
        self.__data = self.clean(data)
    
    def get_data(self) -> pd.DataFrame:
        return self.__data

    # thoughts:
    # the server returns a 500er HTTP-Code
    # this is usually a server-sided problem of the api and not a problem with the request
    # conclusion: we need to handle 5xx and 4xx errors (4xx not really for this assignment)
    def fetch(self, tries=0):
        try:
            resp = requests.get(BillOfMaterialsProvider.API_URL)
            resp.raise_for_status() # this throws exceptions for all HTTP-Codes 400 - 599
            return resp.json()
        # all types of exceptions thrown by .raise_for_status() are subclasses of requests.exceptions.RequestException
        # therefore we only check for that
        # individual except blocks for HTTPError, ConnectionError etc... are not required in this assignment
        except requests.exceptions.RequestException  as e:
            t = tries + 1; sleep(BillOfMaterialsProvider.BACKOFF_FACTOR * (2**(t - 1)))
            return self.fetch(t)
        
    def clean(self, dt) -> pd.DataFrame:
        tmp = {}

        # rewrite indexes
        for key, value in dt.items():
            key = str(key).encode('windows-1252').decode('utf8')
            tmp[key] = value

        # use pandas to clean values
        df = pd.DataFrame(tmp.items(), columns=['material', 'cost'])
        df = df[pd.to_numeric(df['cost'], errors='coerce').notnull()]
        df = df[df['cost'] >= 0] # negative costs are interpreted als wrongly recorded
        df = df.sort_values(by=['cost'])

        return df

if __name__ == '__main__':
    bom = BillOfMaterialsProvider()
    print(bom.get_data())
