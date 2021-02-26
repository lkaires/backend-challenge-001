from rest_framework import serializers
from topic.models import Topic
from post.serializers import PostSerializer
from post.models import Post
from rest_framework.fields import SerializerMethodField

class TopicSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    created_at = serializers.DateTimeField(read_only=True)
    posts = SerializerMethodField()

    def get_posts(self, instance):
        """
            Returns 3 most recent posts
            Intended for list view
        """
        posts = Post.objects.filter(topic=instance.url_name)
        return PostSerializer(posts, read_only=True, many=True, allow_null=True).data[3:]

    class Meta:
        model = Topic
        fields = ['url', 'url_name', 'title', 'description', 'author', 'created_at', 'updated_at', 'posts']

class DetailTopicSerializer(TopicSerializer):
    def get_posts(self, instance):
        """
            Returns all posts
            Intended for detail view
        """
        posts = Post.objects.filter(topic=instance.url_name)
        return PostSerializer(posts, read_only=True, many=True, allow_null=True).data