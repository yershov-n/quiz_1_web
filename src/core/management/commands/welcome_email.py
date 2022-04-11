from datetime import timedelta

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.utils import timezone

yesterday = timezone.now() - timedelta(1)
day_before_yesterday = yesterday - timedelta(1)


class Command(BaseCommand):
    help = "Send Welcome Email To Users"

    def handle(self, *args, **options):

        subject = "Welcome email"

        message = f"Welcome to Quiz! \nAs we can see you not complete any exam yet. \nIf you have " \
                  f"trouble with using our service please contact us and we`ll help you as quickly " \
                  f"as possible"

        users = get_user_model().objects.filter(date_joined__range=(day_before_yesterday, yesterday))

        if users:
            for user in users:
                if not user.results.all():
                    user.email_user(subject=subject, message=message)

        self.stdout.write("Sending welcome emails completed.")
