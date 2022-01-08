from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class User(AbstractBaseUser):
    username = models.CharField()
    password = models.CharField()
    full_name = models.CharField()
    email = models.EmailField()
    phone = models.CharField()
