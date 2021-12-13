import requests

class Currency_converter:
    # empty () to store the conversion rates
    rates = {}

    def __init__(self, url):
        data = requests.get(url).json()

        # Extracting only the rates from the json data
        self.rates = data["rates"]

    # Cross multiplication function
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'USD' :
            amount = amount / self.rates[from_currency]

        # Limit to 2 decimal places
        amount = round(amount * self.rates[to_currency], 2)
        print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))