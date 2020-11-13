from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    Team = models.CharField(max_length=50, default=' ', null=True, blank=True)


