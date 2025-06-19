from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_employer = models.BooleanField(
        default=False,
        verbose_name="Работодатель"
    )
    is_worker = models.BooleanField(
        default=False,
        verbose_name="Соискатель"
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Номер телефона"
    )
    address = models.TextField(
        blank=True,
        verbose_name="Адрес"
    )
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        verbose_name="Фото профиля"
    )
    rating = models.FloatField(
        default=0.0,
        verbose_name="Рейтинг"
    )
    about = models.TextField(
        blank=True,
        verbose_name="О себе"
    )
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
    
    def __str__(self):
        return self.username