"""
API V1: Reddit Serializers
"""
###
# Libraries
###
from rest_framework import serializers

from reddit.models import (
    Topic,
    Post,
    Comment,
)


###
# Nested Serializers
###

# For the challenge, all serializers should go on a respective app (Topic, Post or Comment)

class NestedTopicSerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()

    def get_post_count(self, instance):
        return instance.posts.count()

    class Meta:
        model = Topic
        fields = ['url_name', 'title', 'post_count']


class NestedPostSerializer(serializers.ModelSerializer):
    topic = serializers.StringRelatedField()
    author = serializers.StringRelatedField()
    comment_count = serializers.SerializerMethodField()

    def get_comment_count(self, instance):
        return instance.comment.count()

    class Meta:
        model = Post
        fields = ['id', 'topic', 'title', 'author', 'created_at', 'updated_at', 'comment_count']


class NestedCommentSerializer(serializers.ModelSerializer):
    topic = serializers.SerializerMethodField()
    post = serializers.StringRelatedField()

    def get_topic(self, instance):
        return str(instance.post.topic)

    class Meta:
        model = Comment
        fields = ['id', 'topic', 'post', 'title']


###
# Serializers
###
class TopicSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    post_count = serializers.SerializerMethodField()
    posts = serializers.SerializerMethodField()

    def get_post_count(self, instance):
        # Returns number of posts on topic
        return instance.posts.count()

    def get_posts(self, instance):
        # Returns 3 most recent posts on topic
        return NestedPostSerializer(instance.posts, many=True, allow_null=True).data[:3]

    class Meta:
        model = Topic
        fields = ['url_name', 'title', 'description', 'author', 'created_at', 'updated_at', 'post_count', 'posts']
        read_only_fields = ['url_name', 'created_at', 'post_count', 'posts']


class PostSerializer(serializers.ModelSerializer):
    topic = serializers.StringRelatedField()
    author = serializers.StringRelatedField()
    comment_count = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    def get_comment_count(self, instance):
        # Returns number of comments on post
        return instance.comment.count()

    def get_comments(self, instance):
        # Returns 3 most recent comments on post
        return CommentSerializer(instance.comment, many=True, read_only=True, allow_null=True).data[:3]

    class Meta:
        model = Post
        fields = ['id', 'topic', 'title', 'description', 'author', 'created_at', 'updated_at', 'comment_count', 'comments']
        read_only_fields = ['id', 'created_at', 'comment_count', 'comments']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    post = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'post', 'title', 'description', 'author', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at']