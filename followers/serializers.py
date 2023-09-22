from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """
    Follower Model Serializer
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        """Data Structuring"""
        model = Follower
        fields = [
            'id', 'owner', 'followed', 'followed_name', 'created_at'
        ]

    def create(self, validated_data):
        """Handles Duplications"""
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})
