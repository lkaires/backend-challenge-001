from django.db import models
from helpers.models import BaseInfoModel
from post.models import Post

class Comment(BaseInfoModel):
    post = models.ForeignKey(
        Post,
        related_name='comment',
        on_delete=models.CASCADE
    )

    class Meta:
        # Fix ordering so the most recent is shown first
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title