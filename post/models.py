from django.db import models
from helpers.models import BaseInfoModel

class Post(BaseInfoModel):
    topic = models.ForeignKey('topic.Topic', related_name='post', on_delete=models.CASCADE, null=False, blank=False)