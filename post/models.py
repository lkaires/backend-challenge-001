from django.db import models
from helpers.models import TimestampModel

class Post(TimestampModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey('auth.user', related_name='post', on_delete=models.SET_NULL)
    topic = models.ForeignKey('topic.Topic', related_name='post', on_delete=models.CASCADE)

    class Meta:
        ordering = ['updated_at']