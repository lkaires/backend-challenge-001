"""
Reddit Apps
"""
###
# Libraries
###
from django.apps import AppConfig


###
# Config
###
class RedditConfig(AppConfig):
    name = 'reddit'

    def ready(self):
        import reddit.signals
