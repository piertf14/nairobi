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

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Discusión'
        verbose_name_plural = 'Discusiones'


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

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
