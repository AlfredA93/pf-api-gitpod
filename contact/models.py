from django.db import models
from django.core.mail import send_mail


class Message(models.Model):
    """Contact Us message model"""
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}: {self.subject}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Thank you email to user
        send_mail(
            subject="PhotoFootprint | Thank you for contacting us",
            message="Thank you for contacting us, we'll get back to you soon",
            from_email="teamphotofootprint@hotmail.com",
            recipient_list=[self.email],
        )
