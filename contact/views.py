from rest_framework import generics
from .serializers import MessageSerializer
from .models import Message


class MessageList(generics.ListCreateAPIView):
    """Message List view"""
    serializer_class = MessageSerializer
    queryset = Message.objects.all().order_by('-created_at')
