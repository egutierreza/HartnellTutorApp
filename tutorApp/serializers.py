from rest_framework import serializers
from  tutorApp.models import  Section, Session, Profile
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
	instructing = serializers.PrimaryKeyRelatedField(many=True, queryset=Section.objects.all())
	tutoring = serializers.PrimaryKeyRelatedField(many=True, queryset=Session.objects.all())
	classes = serializers.PrimaryKeyRelatedField(many = True, queryset=Section.objects.all())
	sessionsAttending = serializers.PrimaryKeyRelatedField(many=True, queryset=Session.objects.all())
	sessionsCreated = serializers.PrimaryKeyRelatedField(many=True, queryset=Session.objects.all())
	following = serializers.PrimaryKeyRelatedField(many=True, queryset=Profile.objects.all())
	followers = serializers.PrimaryKeyRelatedField(many=True, queryset =Profile.objects.all())
	#user = serializers.SlugRelatedField(many=False, queryset=User.objects.all(), slug_field='username')
	class Meta:
		model = Profile
		fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
	tutors = serializers.PrimaryKeyRelatedField(many=True, queryset=Profile.objects.all())
	instructor = serializers.PrimaryKeyRelatedField(many=False, queryset=Profile.objects.all())
	class Meta:
		model = Section
		fields = '__all__'

class SessionSerializer(serializers.ModelSerializer):
	section = serializers.SlugRelatedField(many=False, queryset=Section.objects.all(), slug_field='name')
	creator = serializers.SlugRelatedField(many=False, queryset=Profile.objects.all(), slug_field="username")
	attending = serializers.SlugRelatedField(many=True, queryset=Profile.objects.all(), slug_field="username")
	class Meta:
		model = Session
		fields = '__all__'

class SessionDetailSerializer(serializers.ModelSerializer):
	section = serializers.SlugRelatedField(many=False, queryset=Section.objects.all(), slug_field='id')
	creator = serializers.SlugRelatedField(many=False, queryset=Profile.objects.all(), slug_field="id")
	attending = serializers.SlugRelatedField(many=True, queryset=Profile.objects.all(), slug_field="username")
	class Meta:
		model = Session
		fields = '__all__'
