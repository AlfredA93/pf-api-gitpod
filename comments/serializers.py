from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment Model"""
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """Get the is_owner field"""
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        """Set DATETIME format of created_at field to naturaltime"""
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """Set DATETIME format of updated_at field to naturaltime"""
        return naturaltime(obj.updated_at)

    class Meta:
        """Data Structuring from Comment model fields"""
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'post', 'created_at', 'updated_at', 'content'
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for Comment Detail view.
    Post is Read Only, so we don't have to set it on every update.
    """
    post = serializers.ReadOnlyField(source='post.id')
