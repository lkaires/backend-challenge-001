from rest_framework import serializers
from accounts.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    topic = serializers.HyperlinkedRelatedField(many=True, view_name='topics', read_only=True)
    post = serializers.HyperlinkedRelatedField(many=True, view_name='posts', read_only=True)
    comment = serializers.HyperlinkedRelatedField(many=True, view_name='comments', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'topic', 'post', 'comment']