from django.contrib import admin

# Register your models here.

from .models import UserProfile, Blog, Comment


# Minimal registration of Models.
admin.site.register(UserProfile)
admin.site.register(Comment)


class BlogCommentsInline(admin.TabularInline):
    model = Comment
    max_num=0

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'upload_time')
    inlines = [BlogCommentsInline]
