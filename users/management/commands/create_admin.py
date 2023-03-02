from users.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create admin users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--username",
            type=str,
            help="Define the admin username",
        )
        parser.add_argument(
            "--password",
            type=str,
            help="Define the admin password",
        )
        parser.add_argument(
            "--email",
            type=str,
            help="Define the admin email",
        )

    def handle(self, *args, **options):
        my_username = options['username']
        my_password = options['password']
        my_email = options['email']

        username = my_username if my_username else 'admin'
        password = my_password if my_password else 'admin1234'
        email = my_email if my_email else 'admin@example.com'
  
        find_username = User.objects.filter(username=username).first()
        find_email = User.objects.filter(email=email).first()
        
        if find_username:
            raise CommandError(f'Username `{find_username.username}` already taken.')
        if find_email:
            raise CommandError(f'Email `{find_email.email}` already taken.')
        
        User.objects.create_superuser(
                username = username,
                password = password,
                email = email
            )

        self.stdout.write(self.style.SUCCESS(f'Admin `{username}` successfully created!'))