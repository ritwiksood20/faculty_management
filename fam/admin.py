from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import faculty, Teaching, Publication, Education, Achievements, Projects, Application, Schedule, Post, Comment
# Register your models here.

class facultyInline(admin.StackedInline):
    model = Publication
    can_delete = False
    verbose_name_plural = 'faculty'

class PublicationInline(admin.StackedInline):
    model = Publication
    can_delete = False
    verbose_name_plural = 'publication'

class AchievementsInline(admin.StackedInline):
       model = Achievements
       can_delete = False
       verbose_name_plural = 'achievements'


class ProjectsInline(admin.StackedInline):
    model = Projects
    can_delete = False
    verbose_name_plural = 'projects'


class EducationInline(admin.StackedInline):
    model = Education
    can_delete = False
    verbose_name_plural = 'education'

class TeachingInline(admin.StackedInline):
    model = Teaching
    can_delete = False
    verbose_name_plural = 'teaching'
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class facultyInline(admin.StackedInline):
    model = faculty
    can_delete = False
    verbose_name_plural = 'faculty'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (facultyInline, TeachingInline , EducationInline ,PublicationInline ,AchievementsInline,ProjectsInline)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(faculty)
admin.site.register(Teaching)
admin.site.register(Publication)
admin.site.register(Education)
admin.site.register(Achievements)
admin.site.register(Projects    )
admin.site.register(Application)
admin.site.register(Schedule)
admin.site.register(Post)
admin.site.register(Comment)


