from django.core.management.base import BaseCommand
import Crypto.views_favorites as favorites


class Command (BaseCommand):
    help = 'Commands for interacting with the favorites list.\nEnter either add, remove, list or help'

    def add_arguments(self, parser):
        try:
            parser.add_argument('command', choices=[
                                'add', 'remove', 'list', 'help'])
        except:
            print("You have to enter a command")

    def handle(self, *args, **options):
        match options['command']:
            case 'add':
                self.add_to_favorites()

            case 'remove':
                self.remove_from_favorites()

            case 'list':
                self.list_favorites()

            case 'help':
                print(self.help)

    def add_to_favorites(self):
        tags = input('Enter currency TAGs separated by a comma: ')
       # favorites.favorites_insert_tag(tag)
        if (favorites.check_tags(tags)):
            fav = favorites.parse_tags(tags)
            for tag in fav:
                favorites.favorites_insert_tag(tag)
                print("The tag %s has been added to the favorites list" % (tag))

    def remove_from_favorites(self):
        tags = input('Enter currency TAGs separated by a comma: ')
        if (favorites.check_tags(tags)):
            fav = favorites.parse_tags(tags)
            for tag in fav:
                favorites.favorites_remove_tag(tag)
                print("The tag %s has been removed from the favorites list" % (tag))

    def list_favorites(self):
        fav = favorites.favorites_list()
        for tag in fav:
            print(tag)
