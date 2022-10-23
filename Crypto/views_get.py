from django.http import HttpResponse
import requests
from django.template import loader


def get_price_raw(request, cripto_currency, currency):
    response = requests.get(
        "https://api.coinbase.com/v2/prices/%s-%s/spot" % (cripto_currency, currency)).json()
    return response


def get_list_raw(request):
    response = requests.get(
        'https://api.coingecko.com/api/v3/simple/supported_vs_currencies').json()
    return response
