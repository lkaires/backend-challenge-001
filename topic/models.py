from django.db import models
from helpers.models import BaseInfoModel

class Topic(BaseInfoModel):
    url_name = models.SlugField(default='', unique=True, primary_key=True, null=False, auto_created=True)