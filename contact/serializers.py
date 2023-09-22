from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    """Message Serializer"""

    class Meta:
        """Data Structuring"""
        model = Message
        fields = '__all__'
