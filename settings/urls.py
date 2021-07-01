"""
backend-challenge-001 URL Configuration
"""
###
# Libraries
###
from django.conf.urls import url, include
from django.contrib import admin

from helpers.health_check_view import health_check

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
    url(r'^', include(('topic.urls'))),
]
