======================================================
django-migrations-ignore-attrs |release| documentation
======================================================

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

.. toctree::
    :maxdepth: 2

    installation
    commands
    license
