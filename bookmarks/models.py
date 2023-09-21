from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Bookmark(models.Model):
    """
    Bookmark Model, related to the User and Post models.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='bookmarks', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Data Structuring"""
        ordering = ['-created_at']
        unique_together = ['owner', 'post']  # Helps stop duplication

    def __str__(self):
        return f'{self.owner} {self.post}'
