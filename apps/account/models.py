from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.core.constants import STATES

# Create your models here.
class User(AbstractUser):

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField("Email", unique=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=40, choices=STATES)
    phone = models.CharField("Telefone", max_length=50)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone", "username"]

    def __str__(self):
        return "{}".format(self.email)
