from django.db import models
import datetime
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.Aggregate)
    username = models.CharField(max_length=150, blank=True, unique=True)
    isInstructor = models.BooleanField(default=False)
    isTutor = models.BooleanField(default=False)
    isStudent = models.BooleanField(default=False)
    isAdmin = models.BooleanField(default=False)
    school = models.CharField(max_length=80)
    following = models.ManyToManyField('self', related_name = "followers", blank=True, symmetrical=False)
	#profile_image = ImageField(upload_to=get_image_path, blank=True, null=True)
    def __str__(self): 
    	return self.user.username


class Section(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=400)
	subject = models.CharField(max_length=30)
	section_id = models.IntegerField(default=0)
	instructor = models.ForeignKey(Profile, related_name="instructing", blank=True, on_delete=models.CASCADE)
	tutors = models.ManyToManyField(Profile, related_name="tutoring", blank=True)
	students = models.ManyToManyField(Profile, related_name="classes", blank=True)
	def __str__(self):
		return self.name		

#Production Ready
class Session(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=800)
	section = models.ForeignKey(Section, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add =True)
	startSession = models.DateTimeField()
	endSession = models.DateTimeField()
	creator = models.ForeignKey(Profile, related_name="sessionsCreated", blank=True, on_delete=models.CASCADE)
	attending = models.ManyToManyField(Profile, related_name="sessionsAttending", blank=True)
	location = models.CharField(max_length=200)
	#bookmarkedBy = models.ManyToManyField(Profile, related_name="sessionsBookmarked", blank=True)
	def  __str__(self):
		return self.title

 
	



