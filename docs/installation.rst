Installation
============

Install with ``pip`` or ``pipenv``:

.. code:: python

  pip install django-migrations-ignore-attrs

Add ``django_migrations_ignore_attrs`` to your installed apps in your settings.py file:

.. code:: python

  INSTALLED_APPS = [
      'django_migrations_ignore_attrs',
      ...
  ]

Optional configuration:

.. code:: python

  # ignored attributes of model
  MIGRATION_IGNORE_MODEL_ATTRS = ['verbose_name', 'verbose_name_plural']

  # ignored attributes of standard fields
  MIGRATION_IGNORE_FIELD_ATTRS = ['choices', 'help_text', 'verbose_name']

  # ignored attributes of ForeignKey
  MIGRATION_IGNORE_RELATED_FIELD_ATTRS = ['related_name', 'related_query_name']
