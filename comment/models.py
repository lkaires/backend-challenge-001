from django.db import models
from helpers.models import TimestampModel

class Comment(TimestampModel):
    title = models.CharField(blank=True)
    content = models.TextField()
    author = models.ForeignKey('auth.user', related_name='comment', on_delete=models.SET_NULL)
    post = models.ForeignKey('post.Post', related_name='comment', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']