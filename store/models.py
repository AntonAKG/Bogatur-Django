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
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self):
        return f"{self.type} {self.type_day}"

    class Meta:
        verbose_name = 'Абонемент'
        verbose_name_plural = 'Абонементи'


class BasketCoach(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.coach.user.first_name} for {self.user.first_name} {self.user.last_name}'


class BasketTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.ticket.type} {self.ticket.type_day} for {self.user.first_name} {self.user.last_name}'

    def sum(self):
        return self.ticket.price * self.quantity

    @classmethod
    def create_or_update(cls, ticket_id, user):
        baskets = BasketTicket.objects.filter(user=user, ticket_id=ticket_id)

        if not baskets.exists():
            obj = BasketTicket.objects.create(user=user, ticket_id=ticket_id, quantity=1)
            is_created = True
            return obj, is_created
        else:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
            is_crated = False
            return basket, is_crated