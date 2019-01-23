from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, permissions
from socialPosts.models import Comment, Post, Tag
from socialPosts.serializers import PostSerializer, CommentSerializer, TagSerializer, UserSerializer, PostUpdateSerializer, VoteSerializer
from django.contrib.auth.models import User

from tutorApp.models import Profile

class PostList(generics.ListAPIView):
	permission_class = (permissions.AllowAny, )
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostUpdate(generics.CreateAPIView):
	permission_class = (permissions.IsAuthenticated, )
	queryset = Post.objects.all()
	serializer_class = PostUpdateSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_class = (permissions.AllowAny, )
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class CommentList(generics.ListCreateAPIView):
	permission_class = (permissions.AllowAny,)
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_class = (permissions.AllowAny, )
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

class TagList(generics.ListCreateAPIView):
	permission_class = (permissions.AllowAny, )
	queryset = Tag.objects.all()
	serializer_class = TagSerializer

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_class = (permissions.AllowAny, )
	queryset = Tag.objects.all()
	serializer_class = TagSerializer

class UserVotes(generics.ListCreateAPIView):
	permission_class = (permissions.AllowAny, )
	serializer_class = VoteSerializer
	def get_queryset(self):
		current_user=Profile.objects.get(user=self.request.user)
		return Vote.objects.filter(profile = current_user)

class UserPosts(generics.RetrieveAPIView):
	pemrission_class = (permissions.IsAuthenticated, )
	serializer_class = UserSerializer
	def get_object(self):
		return self.request.user

class FeedList(generics.ListCreateAPIView):
	permission_class = (permissions.IsAuthenticated, )
	serializer_class = PostSerializer
	def get_queryset(self):
		current_user = Profile.objects.get(user = self.request.user)
		posts_following = Post.objects.filter(poster__profile__in = current_user.following.all())
		userPosts = Post.objects.filter(poster__profile= current_user)
		allPosts = posts_following | userPosts
		return allPosts.order_by('-created')

