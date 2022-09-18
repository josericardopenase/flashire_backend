from django.core.management.base import BaseCommand, CommandError
from ..models import Something


def cron_test_task():
    Something(name="pepe").save()
