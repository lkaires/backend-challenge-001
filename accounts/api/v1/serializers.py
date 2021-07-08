"""
API V1: Accounts Serializers
"""
###
# Libraries
###
from django.contrib.auth.models import User
from rest_auth.models import TokenModel
from rest_auth.serializers import (
    UserDetailsSerializer as BaseUserDetailsSerializer,
    PasswordResetSerializer as BasePasswordResetSerializer,
)
from rest_framework import serializers
from rest_framework.validators import ValidationError

from accounts.forms import (
    CustomResetPasswordForm,
)

from accounts.models import User as Author
from reddit.api.v1.serializers import (
    NestedTopicSerializer,
    NestedPostSerializer,
    NestedCommentSerializer,
)


###
# Serializers
###
class UserTokenSerializer(serializers.ModelSerializer):
    user = BaseUserDetailsSerializer()

    class Meta:
        model = TokenModel
        fields = ('key', 'user',)


class ChangeEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, email):
        user = self.context['request'].user

        if user.email == email:
            raise ValidationError('Cannot change to the same email.')

        if User.objects.exclude(id=user.id).filter(email=email).exists():
            raise ValidationError('Another account already exists with this email.')

        return email


class PasswordResetSerializer(BasePasswordResetSerializer):
    password_reset_form_class = CustomResetPasswordForm

    def get_email_options(self):
        return {
            'subject_template_name': 'account/password_reset_subject.txt',
            'email_template_name': 'account/password_reset_message.txt',
            'html_email_template_name': 'account/password_reset_message.html',
        }


class UserSerializer(serializers.ModelSerializer):
    topics = serializers.SerializerMethodField()
    posts = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    def get_topics(self, instance):
        return NestedTopicSerializer(instance.topic, many=True, allow_null=True).data
    
    def get_posts(self, instance):
        return NestedPostSerializer(instance.post, many=True, allow_null=True).data

    def get_comments(self, instance):
        return NestedCommentSerializer(instance.comment, many=True, allow_null=True).data

    class Meta:
        model = Author
        fields = ['id', 'username', 'topics', 'posts', 'comments']
        read_only_fields = fields