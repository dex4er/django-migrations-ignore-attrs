from functools import wraps

from django.conf import settings
from django.db.models import Field
from django.db.models.fields.related import RelatedField
from django.db.migrations.operations import AlterModelOptions


DEFAULT_MIGRATION_IGNORE_MODEL_ATTRS = ['verbose_name', 'verbose_name_plural']
DEFAULT_MIGRATION_IGNORE_FIELD_ATTRS = ['choices', 'help_text', 'verbose_name']
DEFAULT_MIGRATION_IGNORE_RELATED_FIELD_ATTRS = ['related_name', 'related_query_name']


def patch_ignored_model_attrs(cls):
    for attr in getattr(settings, 'MIGRATION_IGNORE_MODEL_ATTRS', DEFAULT_MIGRATION_IGNORE_MODEL_ATTRS):
        cls.ALTER_OPTION_KEYS.remove(attr)


def patch_field_deconstruct(old_func):
    @wraps(old_func)
    def deconstruct_with_ignored_attrs(self):
        name, path, args, kwargs = old_func(self)
        for attr in getattr(settings, 'MIGRATION_IGNORE_FIELD_ATTRS', DEFAULT_MIGRATION_IGNORE_FIELD_ATTRS):
            kwargs.pop(attr, None)
        return name, path, args, kwargs
    return deconstruct_with_ignored_attrs


def patch_related_field_deconstruct(old_func):
    @wraps(old_func)
    def deconstruct_with_ignored_attrs(self):
        name, path, args, kwargs = old_func(self)
        for attr in getattr(settings, 'MIGRATION_IGNORE_RELATED_FIELD_ATTRS', DEFAULT_MIGRATION_IGNORE_RELATED_FIELD_ATTRS):
            kwargs.pop(attr, None)
        return name, path, args, kwargs
    return deconstruct_with_ignored_attrs


Field.deconstruct = patch_field_deconstruct(Field.deconstruct)
RelatedField.deconstruct = patch_related_field_deconstruct(RelatedField.deconstruct)
patch_ignored_model_attrs(AlterModelOptions)
