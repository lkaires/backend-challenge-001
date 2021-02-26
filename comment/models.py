from django.db import models
from helpers.models import BaseInfoModel

class Comment(BaseInfoModel):
    post = models.ForeignKey('post.Post', related_name='comment', on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        ordering = ['created_at']