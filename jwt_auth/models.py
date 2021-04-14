from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  #by default AbstractUser do not require email, so the requiement is overwritten here.
    email = models.CharField(max_length=50, unique=True)
    profile_image = models.CharField(max_length=300)
    # todo = models.ForeignKey(
    # "todos.Todo",
    # related_name="user",
    # blank=True,
    # on_delete=models.CASCADE
    # )
