from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """Display a list of all profiles"""
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """Retrieve and/or update the profile if owner"""
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
