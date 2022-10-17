from queue import Empty
from django.core.management.base import BaseCommand
import Crypto.views_users as users


class Command(BaseCommand):
    help = 'Commands for interacting with the users table.\nEnter either add, remove, list or help'

    def add_arguments(self, parser):
        try:
            parser.add_argument('command', choices=[
                                'add', 'remove', 'list', 'help'])
        except:
            print("You have to enter a command")

    def handle(self, *args, **options):
        match options['command']:
            case 'add':
                self.add_user()

            case 'remove':
                self.remove_user()

            case 'list':
                self.list_users()

            case 'help':
                print(self.help)

    def add_user(self):
        username = input('Enter username: ')
        password = input('Enter password: ')
        email = input('Enter email: ')
        if (users.users_insert(username, password, email)):
            print("The user %s has been added to the users table" % (username))
        else:
            print("The user %s already exists" % (username))

    def remove_user(self):
        username = input('Enter username: ')
        if (users.users_remove(username)):
            print("The user %s has been removed from the users table" % (username))
        else:
            print("The user %s does not exist" % (username))

    def list_users(self):
        user = users.users_list()
        if (user is Empty):
            print("The users table is empty")
        else:
            for item in user:
                print(item)
