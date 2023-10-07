from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Redefined User model add field like
    """
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descriptions = models.TextField()
    image = models.ImageField(upload_to=None)
    price_per_training = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренери'


class Ticket(models.Model):
    type = models.CharField(max_length=35)
    type_day = models.CharField(max_length=35)
    price = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Абонемент'
        verbose_name_plural = 'Абонементи'
