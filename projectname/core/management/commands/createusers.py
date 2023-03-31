from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker

class Command(BaseCommand):
    help = 'Creates random base users'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of users to create')

    def handle(self, *args, **options):
        fake = Faker()
        count = options['count']
        for i in range(count):
            username = fake.user_name()
            email = fake.email()
            password = fake.password(length=10)
            User.objects.create_user(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Successfully created user {username}'))
