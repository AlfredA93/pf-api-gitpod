from rest_framework import generics, permissions
from photofootapi.permissions import IsOwnerOrReadOnly
from .models import Bookmark
from .serializers import BookmarkSerializer


class BookmarkList(generics.ListCreateAPIView):
    """Bookmark List view"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()

    def perform_create(self, serializer):
        """Create Bookmark"""
        serializer.save(owner=self.request.user)


class BookmarkDetail(generics.RetrieveDestroyAPIView):
    """
    Get/Delete Bookmark view.
    No need to update as bookmarks are either existant or not
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()
