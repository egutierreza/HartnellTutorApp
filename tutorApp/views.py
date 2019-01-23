from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, permissions

from tutorApp.models import Profile, Section, Session
from django.views.generic import TemplateView
from tutorApp.serializers import ProfileSerializer, SectionSerializer, SessionSerializer, SessionDetailSerializer

class ProfileList(generics.ListCreateAPIView):
	permission_class = (permissions.AllowAny, )
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_class = (permissions.AllowAny, )
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer

class SectionList(generics.ListCreateAPIView):
	permission_class = (permissions.AllowAny, )
	queryset = Section.objects.all()
	serializer_class = SectionSerializer

class SectionDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_class = (permissions.AllowAny, )
	queryset = Section.objects.all()
	serializer_class = SectionSerializer

class SessionList(generics.ListCreateAPIView):
	permission_class = (permissions.AllowAny, )
	serializer_class = SessionSerializer
	queryset = Session.objects.all().order_by('-created')

class SessionDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_class = (permissions.AllowAny, )
	queryset = Session.objects.all()
	serializer_class =  SessionDetailSerializer

class mainView(TemplateView):
	template_name = "tableRough.html"