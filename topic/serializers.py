from rest_framework import serializers
from topic.models import Topic

class TopicSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Topic
        fields = ['title', 'description', 'author', 'url_name', 'created_at', 'updated_at']