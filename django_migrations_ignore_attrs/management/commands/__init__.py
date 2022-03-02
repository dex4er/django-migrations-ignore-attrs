from functools import wraps

from django.conf import settings
from django.db.models import Field, FileField
from django.db.models.fields.related import RelatedField
from django.db.migrations.operations import AlterModelOptions


DEFAULT_MIGRATION_IGNORE_MODEL_ATTRS = ['verbose_name', 'verbose_name_plural']
DEFAULT_MIGRATION_IGNORE_FIELD_ATTRS = ['choices', 'help_text', 'verbose_name']
DEFAULT_MIGRATION_IGNORE_FILE_FIELD_ATTRS = ["upload_to", "storage"]
DEFAULT_MIGRATION_IGNORE_RELATED_FIELD_ATTRS = ['related_name', 'related_query_name']


def patch_ignored_model_attrs(cls):
    for attr in getattr(settings, 'MIGRATION_IGNORE_MODEL_ATTRS', DEFAULT_MIGRATION_IGNORE_MODEL_ATTRS):
        cls.ALTER_OPTION_KEYS.remove(attr)


def patch_deconstruct(deconstruct_function, setting_name, default_setting):
    @wraps(deconstruct_function)
    def deconstruct_with_ignored_attrs(self):
        name, path, args, kwargs = deconstruct_function(self)
        for attr in getattr(settings, setting_name, default_setting):
            kwargs.pop(attr, None)
        return name, path, args, kwargs
    return deconstruct_with_ignored_attrs


Field.deconstruct = patch_deconstruct(
    deconstruct_function=Field.deconstruct,
    setting_name='MIGRATION_IGNORE_FIELD_ATTRS',
    default_setting=DEFAULT_MIGRATION_IGNORE_FIELD_ATTRS
)
FileField.deconstruct = patch_deconstruct(
    deconstruct_function=FileField.deconstruct,
    setting_name='MIGRATION_IGNORE_FILE_FIELD_ATTRS',
    default_setting=DEFAULT_MIGRATION_IGNORE_FILE_FIELD_ATTRS
)
RelatedField.deconstruct = patch_deconstruct(
    deconstruct_function=RelatedField.deconstruct,
    setting_name='MIGRATION_IGNORE_RELATED_FIELD_ATTRS',
    default_setting=DEFAULT_MIGRATION_IGNORE_RELATED_FIELD_ATTRS
)

patch_ignored_model_attrs(AlterModelOptions)
