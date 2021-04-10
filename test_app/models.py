from django.db import models
from django.db.models import CharField

from cached_markdown_field.models import CachedMarkdownField


class NameAndDescription(models.Model):
    name = CharField(max_length=20)
    description = CachedMarkdownField()


class VerboseNameAndHelpDescription(models.Model):
    description = CachedMarkdownField(verbose_name="Description", help_text="This should help you")
