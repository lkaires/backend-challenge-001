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

###
# Router
###
router = routers.SimpleRouter()
router.register(r'topics', TopicViewSet)

topics_router = routers.NestedSimpleRouter(router, r'topics', lookup='topic')

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
    url(r'^', include('user.urls')),

    # Applications
    url(r'^', include('accounts.urls')),
    url(r'^', include(router.urls)),
    url(r'^', include(topics_router.urls)),
]
