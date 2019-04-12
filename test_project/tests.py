from django.core.management import call_command
from django.test import TestCase


class TestDjangoMigrationsIgnoreAttrs(TestCase):

    @staticmethod
    def test_migrate():
        call_command('migrate', 'test_project', verbosity=0)

    @staticmethod
    def test_makemigrations():
        call_command('makemigrations', 'test_project', check=True, dry_run=True, verbosity=0)
