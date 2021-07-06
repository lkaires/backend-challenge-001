"""
Reddit admin
"""
###
# Libraries
###
from django.contrib import admin

from reddit.models import (
    Topic,
    Post,
    Comment,
)


###
# Inline Admin Models
###


###
# Main Admin Models
###
admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Comment)