import requests


class CurrencyConverter:
    # empty dict to store the conversion rates
    rates = {}

    def __init__(self, url):
        data = requests.get(url).json()

        # Extracting only the rates from the json data
        self.rates = data["rates"]

        # function to do a simple cross multiplication between

    # the amount and the conversion rates
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]

        # limiting the precision to 2 decimal places
        amount = round(amount * self.rates[to_currency], 2)
        print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))


# Driver code
if __name__ == "__main__":
    # YOUR_ACCESS_KEY = 'GET YOUR ACCESS KEY FROM fixer.io'
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', '6de1d8851a44e27833d50917e47ac83d')
    c = CurrencyConverter(url)
    print("Welcome to the Currency Converter! Here are the accepted currency formats: ")
    print("USD = US Dollar |", "EUR = Euro |", "GBP = UK Pound |", "CAD = Canadian Dollar |", "AUD = Australian Dollar |", "PLN = Polish Złoty |","MXN = Mexican Dollar |")
    from_country = input("From Country: ")
    to_country = input("TO Country: ")
    amount = int(input("Amount: "))

    c.convert(from_country, to_country, amount)
