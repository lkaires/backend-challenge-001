from django.db import models
from helpers.models import TimestampModel

class Topic(TimestampModel):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    author = models.ForeignKey('accounts.User', related_name='topic', on_delete=models.SET_NULL, null=True)
    url_name = models.SlugField(default='', unique=True)

    class Meta:
        ordering = ["updated_at"]