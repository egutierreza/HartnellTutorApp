from rest_framework import serializers
from  socialPosts.models import  Tag, Comment, Post
from django.contrib.auth.models import User
from tutorApp.models import Profile

from tutorApp.models import Profile

class TagSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Tag
		fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
	poster = serializers.PrimaryKeyRelatedField(many=False, queryset = Profile.objects.all())
	responses = serializers.PrimaryKeyRelatedField(many=True, queryset = Comment.objects.all())
	class Meta:
		model = Comment
		fields = '__all__'

class PostUpdateSerializer(serializers.ModelSerializer):
	poster = serializers.PrimaryKeyRelatedField(many=False, queryset=Profile.objects.all())
	tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
	comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())
	class Meta:
		model = Post
		fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
	poster = serializers.PrimaryKeyRelatedField(many=False, queryset=Profile.objects.all())
	tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
	comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())
	class Meta:
		model = Post
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
	posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
	comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())
	profile = serializers.PrimaryKeyRelatedField(many = False, queryset = Profile.objects.all())
	class Meta:
		model = User
		fields = '__all__'

class VoteSerializer(serializers.ModelSerializer):
	profile = serializers.PrimaryKeyRelatedField(many=False, queryset=Profile.objects.all())
	comment = serializers.PrimaryKeyRelatedField(many=False, queryset=Comment.objects.all())
	post = serializers.PrimaryKeyRelatedField(many=False, queryset=Post.objects.all())
