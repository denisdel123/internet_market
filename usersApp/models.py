from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {
    'null': True,
    'blank': True,
}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='Аватар')
    is_confirm = models.BooleanField(default=False, verbose_name='Подтверждение')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
