from django.db import models
import datetime
from django.contrib.auth.models import User
from tutorApp.models import Profile

class Tag(models.Model):
	word = models.CharField(max_length=35)
	created_at = models.DateTimeField(auto_now_add = False)

	def __str__(self):
		return self.word

class Post(models.Model):
	title = models.CharField(max_length=100)
	topic = models.CharField(max_length=50)
	details = models.CharField(max_length=1200)
	poster = models.ForeignKey(Profile, related_name="posts", on_delete=models.CASCADE)
	score = models.IntegerField(default=0)
	created = models.DateTimeField(auto_now_add=True)
	tags = models.ManyToManyField(Tag, blank=True, related_name="posts")
	post_type = models.CharField(max_length  = 1, default = "")
	
	def __str__(self):
		return self.title

class Comment(models.Model):
	poster = models.ForeignKey(Profile, related_name="comments", on_delete=models.CASCADE)
	text = models.CharField(max_length=1600)
	responses = models.ManyToManyField('self', blank=True)
	score = models.IntegerField(default = 0)
	deleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey(Post, related_name = "comments", blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.poster.username + str(self.pk)

class Vote(models.Model):
	profile = models.ForeignKey(Profile, related_name="votes", on_delete=models.CASCADE);
	comment = models.ForeignKey(Comment, related_name="votes", on_delete=models.CASCADE, null=True, blank=True);
	post = models.ForeignKey(Post, related_name = "votes", on_delete=models.CASCADE, null=True, blank=True);
	value = models.BooleanField(blank=True)

class Notification(models.Model):
	actor = models.ForeignKey(Profile, related_name = "notifying", blank=True, on_delete=models.CASCADE)
	verb = models.CharField(max_length=30)
	action_post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
	action_comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.CASCADE)
	target = models.ForeignKey(Profile, blank=True,  null=True, related_name="notifier", on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	viewed = models.DateTimeField(blank=True, null=True)