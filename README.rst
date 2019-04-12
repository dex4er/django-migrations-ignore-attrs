.. image:: https://img.shields.io/pypi/v/django-migrations-ignore-attrs.svg
   :target: https://pypi.python.org/pypi/django-migrations-ignore-attrs
.. image:: https://travis-ci.org/dex4er/django-migrations-ignore-attrs.svg?branch=master
   :target: https://travis-ci.org/dex4er/django-migrations-ignore-attrs
.. image:: https://readthedocs.org/projects/django-migrations-ignore-attrs/badge/?version=latest
   :target: http://django-migrations-ignore-attrs.readthedocs.org/en/latest/
.. image:: https://img.shields.io/pypi/pyversions/django-migrations-ignore-attrs.svg
   :target: https://www.python.org/
.. image:: https://img.shields.io/pypi/djversions/django-migrations-ignore-attrs.svg
   :target: https://www.djangoproject.com/

django-migrations-ignore-attrs
==============================

django-migrations-ignore-attrs is a package that overrides ``makemigration``
and ``migrate`` commands for Django's ``manage.py`` command.

django-migrations-ignore-attrs allows to avoid making of unnecessary migrations
for attributes that do not have any representation in database schema.

Following attributes of model are ignored:

* verbose_name
* verbose_name_plural

Following attributes of standard fields are ignored:

* choices
* help_text
* verbose_name

Following attributes of ``ForeignKey`` are ignored:

* related_name
* related_query_name


Installation
------------

Install with ``pip`` or ``pipenv``:

.. code:: python

  pip install django-migrations-ignore-attrs

Add ``django_migrations_ignore_attrs`` to your installed apps in your
settings.py file:

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


Commands
--------

makemigrations
^^^^^^^^^^^^^^

Creates new migration(s) for apps.

All options are the same as for original ``makemigrations`` command from
``django`` app.

migrate
^^^^^^^

Updates database schema. Manages both apps with migrations and those without.

All options are the same as for original ``migrate`` command from ``django``
app.


Documentation
-------------

See http://django-migrations-ignore-attrs.readthedocs.org/


License
-------

Copyright © 2019, Piotr Roszatycki

This software is distributed under the GNU Lesser General Public License (LGPL
3 or greater).
