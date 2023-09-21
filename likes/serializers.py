from django.db import IntegrityError
from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    """Like Model Serializer"""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Data Structuring"""
        model = Like
        fields = ['id', 'owner', 'post', 'created_at']

    def create(self, validated_data):
        """Create Like if one doesn't already exist"""
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'Possible Duplicate'
            })
