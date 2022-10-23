from time import time
from django.core.management.base import BaseCommand
import Crypto.views_logic as logic
from django.utils import timezone


class Command(BaseCommand):

    help = 'Currrency related commands enter either price, list or help'

    def add_arguments(self, parser):

        parser.add_argument('command', choices=['price', 'list', 'help'])

    def handle(self, *args, **options):

        match options['command']:
            case 'price':
                self.get_price()

            case 'list':
                self.get_currency_list()

            case 'help':
                print(self.help)

    def get_price(self):
        cripto_currency = input('Enter the crypto currency: ')
        currency = input('Enter the currency: ')
        response = logic.get_price(cripto_currency, currency)
        time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        try:

            print('The price of %s is %s %s at %s' %
                  (cripto_currency, response['data']['amount'], currency, time))

        except:
            print('Please enter a valid currency pair')

    def get_currency_list(self):
        response = logic.get_list_raw(None)
        print('The supported currencies are:')
        for item in response:
            print(item)
