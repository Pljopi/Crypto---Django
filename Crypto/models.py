from email.policy import default
from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.username


class Currencies(models.Model):
    tag = models.CharField(max_length=200)
    # add id which is foreign key to users
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag


class Favorites(models.Model):
    tag = models.CharField(max_length=200)
    user_id = models.ForeignKey(Users, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag
