from django.db.models import Count
from rest_framework import generics
from photofootapi.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """Display a list of all profiles"""
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """Retrieve and/or update the profile if owner"""
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
