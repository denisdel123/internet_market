import os

from django.core.management import BaseCommand

from usersApp.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@mail.ru',
            first_name='Admin',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        user.set_password(os.getenv('PASS_SUPERUSER'))
        user.save()