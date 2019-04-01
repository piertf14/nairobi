from django.db import models
from django.contrib.auth.models import User


class Discussion(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    message = models.TextField(
    )
    likes = models.PositiveIntegerField(
        default=0
    )
    is_active = models.BooleanField(
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def get_comments(self):
        return self.comments.filter(is_active=True)


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    discussion = models.ForeignKey(
        Discussion,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    message = models.TextField(
    )
    likes = models.PositiveIntegerField(
        default=0
    )
    is_active = models.BooleanField(
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )