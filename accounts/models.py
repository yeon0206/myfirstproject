from django.conf import settings
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    phone = models.IntegerField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    description = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to="accounts/profile/%Y/%m/%d", blank=True)
    
