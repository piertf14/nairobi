from django.contrib import admin
from discussion.models import Discussion, Comment


@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_active', 'created_at')
    raw_id_fields = ('user',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_active', 'created_at')
    raw_id_fields = ('user',)
