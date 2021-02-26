"""
backend-challenge-001 URL Configuration
"""
###
# Libraries
###
from django.conf.urls import url, include
from django.contrib import admin

from helpers.health_check_view import health_check

from rest_framework_nested import routers

from topic.views import TopicViewSet
from post.views import PostViewSet
from comment.views import CommentViewSet

###
# Router
###
router = routers.DefaultRouter()
router.register(r'topics', TopicViewSet)

topic_router = routers.NestedSimpleRouter(router, r'topics')
topic_router.register(r'posts', PostViewSet)

post_router = routers.NestedSimpleRouter(topic_router, r'posts')
post_router.register(r'comments', CommentViewSet)

###
# URLs
###
urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Health Check
    url(r'health-check/$', health_check, name='health_check'),

    # Login
    url(r'api-auth/', include('rest_framework.urls')),

    # Applications
    url(r'^', include('accounts.urls')),
    url(r'^', include('user.urls')),
    url(r'^', include(router.urls)),
    url(r'^', include(topic_router.urls)),
    url(r'^', include(post_router.urls)),
]
