from django.core.management import call_command
from django.test import TestCase


class TestDjangoMigrationsIgnoreAttrs(TestCase):

    @staticmethod
    def test_migrate():
        call_command('migrate', 'test_project', verbosity=0)

    @staticmethod
    def test_makemigrations_no_changes():
        call_command('makemigrations', 'test_project', check=True, dry_run=True, verbosity=0)

    def test_makemigrations_field_changes(self):
        with self.settings(
            MIGRATION_IGNORE_FIELD_ATTRS=[],
        ):
            with self.assertRaises(SystemExit):
                call_command('makemigrations', 'test_project', check=True, dry_run=True, verbosity=0)

    def test_makemigrations_file_field_changes(self):
        with self.settings(
            MIGRATION_IGNORE_FILE_FIELD_ATTRS=[],
        ):
            with self.assertRaises(SystemExit):
                call_command('makemigrations', 'test_project', check=True, dry_run=True, verbosity=0)

    def test_makemigrations_related_field_changes(self):
        with self.settings(
            MIGRATION_IGNORE_RELATED_FIELD_ATTRS=[],
        ):
            with self.assertRaises(SystemExit):
                call_command('makemigrations', 'test_project', check=True, dry_run=True, verbosity=0)
