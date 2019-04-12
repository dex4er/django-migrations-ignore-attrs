from django.db import models
from django.contrib import auth


# initial migration is for CHANGED = ''
CHANGED = '_changed'

LANGUAGE_CHOICES = (
    ('EN', "English" + CHANGED),
    ('DE', "German" + CHANGED),
    ('FR', "French" + CHANGED),
    ('PL', "Polish" + CHANGED),
)


class Category(models.Model):
    name = models.CharField(max_length=100, help_text='Category name' + CHANGED)

    class Meta:
        verbose_name_plural = "categories" + CHANGED

    def __str__(self):
        return self.name


class Note(models.Model):
    user = models.ForeignKey(auth.models.User, on_delete=models.CASCADE, related_name='notes' + CHANGED, related_query_name='node' + CHANGED, verbose_name="Django user" + CHANGED)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notes' + CHANGED, related_query_name='node' + CHANGED)
    keywords = models.CharField(max_length=400)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    content = models.TextField(max_length=50000)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)

    def __str__(self):
        return self.title
