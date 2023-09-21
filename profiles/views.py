from rest_framework import generics
from .models import Profile


class ProfileList(generics.ListAPIView):
    """Display a list of all profiles"""
    queryset = Profile.objects.all()
