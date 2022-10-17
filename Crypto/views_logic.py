from Crypto.views import get_list_raw
from Crypto.views import get_price_raw


def get_price(cripto_currency, currency):
    """
    This function returns the price of a crypto currency in a given currency
    """

    price_pair_validation(cripto_currency, currency)
    response = get_price_raw(None, cripto_currency, currency)
    return response


def price_pair_validation(cripto_currency, currency):
    """
    This function validates the pair of currencies
    """

    if is_lenght_between(cripto_currency) and is_lenght_between(currency):
        cripto_currency = cripto_currency.lower()
        currency = currency.lower()
    else:
        print("Please enter a valid currency pair a currency TAG cannot be shorter than 2 or longer than 5 charcters long")
        quit()
    if (cripto_currency == currency):
        print("Please enter a valid currency pair, the currencies cannot be the same")
        quit()
    if is_currency_on_list_of_supported_currencies(cripto_currency) and is_currency_on_list_of_supported_currencies(currency):
        return True
    else:
        print("Please enter a valid currency pair, the currencies are not supported")
        quit()


def is_lenght_between(string, min=2, max=6):
    """
     This function validates the lenght of each currency TAG
     """

    if len(string) >= min and len(string) <= max:
        return True
    else:
        return False


def is_currency_on_list_of_supported_currencies(currency):
    """
    This function validates if the currency is on the list of supported currencies
    """

    response = get_list_raw(None)
    if currency in response:
        return True
    else:
        return False
