from django.db import models
from helpers.models import BaseInfoModel

from topic.models import Topic

class Post(BaseInfoModel):
    topic = models.ForeignKey(
        Topic,
        related_name='posts',
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.title