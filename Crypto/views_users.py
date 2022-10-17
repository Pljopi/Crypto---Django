from Crypto.models import Users


def users_insert(username, password, email):
    try:
        Users.objects.create(username=username, password=password, email=email)
        return True
    except:
        return False


def users_remove(username):
    try:
        Users.objects.filter(username=username).delete()
        return True
    except:
        return False


def users_list():
    return Users.objects.all()
