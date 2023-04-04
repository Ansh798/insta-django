from django.db import models
from django.contrib.auth.models import AbstractUser
from insta.manager import UserManager


# Create your models here.
def User(AbstractUser):
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=True)


    REQUIRED_FIELDS = []
    objects= UserManager()