from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

from django.db.models.signals import post_save

# Create your models here.
class faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='faculty')
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    department = models.CharField(max_length=100)
    mobileNo = models.CharField(max_length=100,default=' ')
    designation = models.CharField(max_length=100, default=' ')
    gender = models.CharField(max_length=100, default=' ')
    email = models.CharField(max_length=60, null=True)
    title = models.CharField(max_length=30, null=True)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=150, null=True)
    mother_tongue = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, null=True)

    avatar = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    

    class Meta:
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return self.user.username



class Teaching(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='teaching')
    course = models.CharField(max_length=100)
    start_date =  models.CharField(max_length=100,default=' ')
    end_date = models.CharField(max_length=100,default=' ')

    def __str__(self):
        return self.user.username

class Publication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publication')
    pub = models.CharField(max_length=300)
    where = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='education')
    degree = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    year = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=300)
    sponser = models.CharField(max_length=300)
    duration = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username




class Achievements(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievements')
    ach = models.CharField(max_length=300)
    year =  models.CharField(max_length=100)
    details = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username



class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='application')
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100)
    body = models.TextField()
    Status = models.IntegerField(default=0)
    date = models.DateField(default= datetime.now)

    def __str__(self):
        return '%s | %s | %s' %(self.user.username, self.date, self.Status)

class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='schedule')
    subject = models.CharField(max_length=100)
    time = models.CharField(max_length=5)
    day = models.CharField(max_length=10)
    
    def __str__(self):
        return self.user.username

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateField(default= datetime.now)

    def __str__(self):
        return str(self.title)

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    body = models.TextField()
    date = models.DateField(default= datetime.now)

    def __str__(self):
        return self.user.username






