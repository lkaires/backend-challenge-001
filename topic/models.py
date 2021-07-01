from django.db import models
from helpers.models import BaseInfoModel
from django.utils.text import slugify

class Topic(BaseInfoModel):
    url_name = models.SlugField(
        unique=True
    )

    def save(self, *args, **kwargs):
        # Creates url_name based on topic title, instead of setting default
        if not self.url_name:
            self.url_name = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title