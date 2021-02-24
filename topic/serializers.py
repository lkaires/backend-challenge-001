from rest_framework import serializers
from topic.models import Topic

class TopicSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Topic
        fields = ['title', 'description', 'owner', 'url_name', 'created_at', 'updated_at']