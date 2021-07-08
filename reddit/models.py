"""
Reddit Models
"""
###
# Libraries
###
from django.db import models
from django.utils.text import slugify

from helpers.models import BaseInfoModel


###
# Choices
###


###
# Querysets
###


###
# Models
###

# For the challenge, these models should be each in a respective app

class Topic(BaseInfoModel):
    url_name = models.SlugField(
        unique=True
    )

    def save(self, *args, **kwargs):
        # Creates url_name based on topic title, instead of setting default
        if not self.url_name:
            self.url_name = slugify(self.title)
        super().save(*args, **kwargs)


class Post(BaseInfoModel):
    topic = models.ForeignKey(
        Topic,
        related_name='posts',
        on_delete=models.CASCADE,
    )


class Comment(BaseInfoModel):
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE
    )

    class Meta:
        # Fix ordering so the most recent is shown first
        ordering = ['-created_at']