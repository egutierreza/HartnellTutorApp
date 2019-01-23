from django.contrib import admin
from .models import  Post, Comment, Tag, Vote, Notification

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'poster', 'created']
	ordering = ['created']
admin.site.register(Post, PostAdmin)
class CommentAdmin(admin.ModelAdmin):
	list_display = ['poster', 'created']
	ordering = ['created']
admin.site.register(Comment, CommentAdmin)
class TagAdmin(admin.ModelAdmin):
	list_display = ['word', 'created_at']
	list_ordering = ['created_at']
admin.site.register(Tag, TagAdmin)
class VoteAdmin(admin.ModelAdmin):
	list_display = ['post','profile', 'value']
	list_ordering = ['post']
admin.site.register(Vote, VoteAdmin)
class NotificationAdmin(admin.ModelAdmin):
	list_display = ['actor','verb','target', 'created']
	list_ordering = ['created']
admin.site.register(Notification, NotificationAdmin)
