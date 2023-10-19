from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

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
    slug = models.SlugField(unique=True, max_length=50)
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренери'


class Ticket(models.Model):
    type = models.CharField(max_length=35)
    type_day = models.CharField(max_length=35)
    price = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.type} {self.type_day}"

    class Meta:
        verbose_name = 'Абонемент'
        verbose_name_plural = 'Абонементи'