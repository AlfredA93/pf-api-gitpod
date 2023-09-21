from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """JSON serializer for Profile model"""
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """Get the is_owner field"""
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """Data structure for profile serializer"""
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'bio', 'image', 'is_owner',
        ]
