"""
API V1: Reddit Urls
"""
###
# Libraries
###
from django.urls import re_path, include
from rest_framework_nested import routers

from reddit.api.v1.views import (
    TopicViewSet,
    PostViewSet,
    CommentViewSet,
)


###
# Routers
###
""" Main router """
router = routers.SimpleRouter()
router.register(r'topics', TopicViewSet, basename='topic')

topic_router = routers.NestedSimpleRouter(router, r'topics', lookup='topic')
topic_router.register(r'posts', PostViewSet, basename='post')

post_router = routers.NestedSimpleRouter(topic_router, r'posts', lookup='post')
post_router.register(r'comments', CommentViewSet, basename='comment')



###
# URLs
###
urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^', include(topic_router.urls)),
    re_path(r'^', include(post_router.urls)),
]