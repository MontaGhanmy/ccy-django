from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    user_type = models.TextField()
    user_successrate = models.TextField()
    user_desc = models.TextField(default="my description")
    user_tags = models.TextField(default="ccy, ")
    image = models.FileField(null=True, blank=True)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)