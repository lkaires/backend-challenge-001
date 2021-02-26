from rest_framework_nested.routers import DefaultRouter, NestedSimpleRouter

from topic.views import TopicViewSet
from post.views import PostViewSet
from comment.views import CommentViewSet

from django.urls import path, include

###
# Router
###
router = DefaultRouter()
router.register(r'topics', TopicViewSet, basename='topic')

topic_router = NestedSimpleRouter(router, r'topics', lookup='topic')
topic_router.register(r'posts', PostViewSet, basename='post')

post_router = NestedSimpleRouter(topic_router, r'posts', lookup='post')
post_router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(topic_router.urls)),
    path('', include(post_router.urls)),
]