from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model - related to 'owner' and 'followed'
    'owner' = a User that is following another User
    'followed' = a User that is being followed by 'owner'
    We use related_name to differentiate between fields with greater ease.
    """
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
        )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Data Structuring"""
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']  # Helps stop duplication

    def __str__(self):
        return f'{self.owner} {self.followed}'
