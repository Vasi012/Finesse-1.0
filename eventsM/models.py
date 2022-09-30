from django.db import models


class SubscribedUsers(models.Model):
    email = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=50)
