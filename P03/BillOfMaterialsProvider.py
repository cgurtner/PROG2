import requests


class BillOfMaterialsProvider:
    API_URL = 'http://160.85.252.148'

    def __init__(self):
        self.__data = self.fetch()
    
    def get_data(self) -> dict:
        return self.__data

    # thoughts:
    # the server returns a 500er HTTP-Code
    # this is usually a server-sided problem of the api and not a problem with the request
    # conclusion: we need to handle 5xx and 4xx errors (4xx not really for this assignment)
    def fetch(self):
        try:
            resp = requests.get(BillOfMaterialsProvider.API_URL)
            resp.raise_for_status() # this throws exceptions for all HTTP-Codes 400 - 599
            return resp.json()
        # all types of exceptions thrown by .raise_for_status() are subclasses of requests.exceptions.RequestException
        # therefore we only check for that
        # individual except blocks for HTTPError, ConnectionError etc... are not required in this assignment
        except requests.exceptions.RequestException  as e:
            return self.fetch()

if __name__ == '__main__':
    bom = BillOfMaterialsProvider()
    print(bom.get_data())