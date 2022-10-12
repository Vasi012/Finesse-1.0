from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class SubscribedUsers(models.Model):
    """Newsletter subscribed users"""
    email = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=50)


class Profile(models.Model):
    """Add links and profile picture for users"""
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True,
                                    upload_to="images/profile_pic")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        """get absolute url for user new profile"""
        return reverse('eventsM')
