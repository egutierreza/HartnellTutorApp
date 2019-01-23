from django.contrib import admin
from .models import Profile, Section, Session

class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'isInstructor', 'isStudent', 'isTutor', 'isAdmin']
	ordering = ['user']
admin.site.register(Profile, ProfileAdmin)
class SectionAdmin(admin.ModelAdmin):
	list_display = ['name','instructor', 'subject']
	ordering=['name']
admin.site.register(Section, SectionAdmin)
class SessionAdmin(admin.ModelAdmin):
	list_display = ['title', 'created', 'location', 'startSession', 'endSession']
	ordering=['created']
admin.site.register(Session, SessionAdmin)



#3e016af8c8757570668314a1dde24705b759670d6f71835808847b9f50eef834



