from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.freecurrencyapi.com/"
API_KEY = "KRWvt4S0l5xrdKYsTuj6Hv7gpkKR5p5zbAhrJrpc"

printer = PrettyPrinter()


def get_currencies():
    endpoint = f"v1/currencies?apikey={API_KEY}"
    url = BASE_URL + endpoint
    recived_data = get(url).json()['data']
    recived_data = list(recived_data.items())
    recived_data.sort()
    # printer.pprint(recived_data)
    return recived_data


def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['name']
        code = currency['code']
        symbol = currency.get('symbol', "")
        print(f"{code} - {name} - {symbol}")

# ! Alert almost everything does not work in this code. Because the API has a restriction and it is deprecated.


def exchange_rate(currency1, currency2):
    endpoint = f"v1/convert?q={currency1}_{currency2}&compact=ultra&apikey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()

    if len(data) == 0:
        print("Invalid currencies.")
        return

    rate = list(data.values())[0]
    print(f"{currency1} -> {currency2} = {rate}")

    return rate


def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except:
        print("Invalid amout.")
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount


def main():
    currencies = get_currencies()

    print("welcome to currency concerter.")
    print("List - lists the different currencies.")
    # ?only list work the other two..convert and rate does not work for the API limitations.
    print("Convert - convert from one currency to another.")
    print("Rate - get the exachange rate of two currencies.")
    print()

    while True:
        command = input("Please enter a command to q to quite: ").lower()

        if command == "q":
            break
        elif command == "list":
            print(print_currencies(currencies))
        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter a in amount{currency1}")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Unrecognized command")


main()
