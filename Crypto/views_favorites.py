from Crypto.models import Favorites
from Crypto.views import get_list_raw
import ast


def favorites_insert_tag(tag):

    fav = Favorites(tag=tag)
    fav.save()


def favorites_remove_tag(tag):
    Favorites.objects.filter(tag=tag).delete()


def favorites_list():
    return Favorites.objects.all()


def check_tags(tags):
    if (tags):
        return True
    else:
        print("You have to enter at least one tag for this to work")


def parse_tags(tags):
    tags = tags.split(',')
    tags = [tag.strip() for tag in tags]
    tags = ast.literal_eval(str(tags))
    fav = []
    list_of_currencyes = get_list_raw(None)
    for tag in tags:
        if (tag in list_of_currencyes):
            fav.append(tag)
        else:
            print("The tag %s is not supported" % (tag))
    fav = list(dict.fromkeys(fav))
    return fav
