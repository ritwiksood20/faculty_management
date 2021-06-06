from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from .models import faculty,Education,Teaching,Publication,Projects,Achievements, Application, Schedule, Post, Comment
# Create your views here.

def index(request):
    return render(request, 'fam/index.html')

def login_request(request):
    context={}
    if request.method == 'POST':
        usr = request.POST.get('form-username')
        pwd = request.POST.get('form-password')
        user = authenticate(username=usr, password=pwd)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            context["error"] = 'Invalid Username or Password'
            return render(request, 'fam/index.html',context)
    else:
        return render(request, 'fam/index.html',context)
    
def home(request):
    context ={}
    context['user'] = request.user
    context['faculty'] = faculty.objects.all()
    if request.user.is_authenticated:
        return render(request, 'fam/home.html',context)
    else:
        return render(request, 'fam/index.html')

def logout_request(request):
        logout(request)
        return render(request, 'fam/index.html')
        
def about(request):
    context ={}
    if request.user.is_authenticated:
        return render(request, 'fam/about.html',context)
    else:
        return render(request, 'fam/index.html')

def profile(request):
    context ={}
    if request.user.is_authenticated:
        context['user'] = request.user
        context['faculty'] = faculty.objects.all()
        return render(request, 'fam/profile.html',context)
    else:
        return render(request, 'fam/index.html')

def subject(request):
    context ={}
    if request.user.is_authenticated:
        context['user'] = request.user
        context['subject'] = Teaching.objects.filter(user = request.user.id)
        return render(request, 'fam/subject.html',context)
    else:
        return render(request, 'fam/index.html')

def education(request):
    context ={}
    if request.user.is_authenticated:
        context['user'] = request.user
        context['education'] = Education.objects.filter(user = request.user.id)
        return render(request, 'fam/education.html',context)
    else:
        return render(request, 'fam/index.html')

def publication(request):
    context ={}
    if request.user.is_authenticated:
        context['user'] = request.user
        context['publication'] = Publication.objects.filter(user = request.user.id)
        return render(request, 'fam/publication.html',context)
    else:
        return render(request, 'fam/index.html')

def projects(request):
    context ={}
    if request.user.is_authenticated:
        context['user'] = request.user
        context['projects'] = Projects.objects.filter(user = request.user.id)
        return render(request, 'fam/projects.html',context)
    else:
        return render(request, 'fam/index.html')

def achievement(request):
    context ={}
    if request.user.is_authenticated:
        context['user'] = request.user
        context['achievements'] = Achievements.objects.filter(user = request.user.id)
        return render(request, 'fam/achievement.html',context)
    else:
        return render(request, 'fam/index.html')

def attendance(request):
    context ={}
    context['user'] = request.user
    context['faculty'] = faculty.objects.all()
    if request.user.is_authenticated:
        return render(request, 'fam/attendance.html',context)
    else:
        return render(request, 'fam/index.html')

def forum(request):
    context ={}
    context['user'] = request.user
    context['faculty'] = faculty.objects.all()
    context['forum'] = Post.objects.all()
    if request.user.is_authenticated:
        return render(request, 'fam/forum.html',context)
    else:
        return render(request, 'fam/index.html')

def schedules(request):
    context ={}
    context['user'] = request.user
    context['faculty'] = faculty.objects.all()
    context['schedule'] = Schedule.objects.all()
    if request.user.is_authenticated:
        return render(request, 'fam/schedules.html',context)
    else:
        return render(request, 'fam/index.html')

def application(request):
    context ={}
    context['user'] = request.user
    context['faculty'] = faculty.objects.all()
    context['application'] = Application.objects.filter(user = request.user.id)
    if request.user.is_authenticated:
        return render(request, 'fam/application.html',context)
    else:
        return render(request, 'fam/index.html')

def viewapplication(request):
    context ={}
    context['user'] = request.user
    context['faculty'] = faculty.objects.all()
    ap = request.GET.get('appid')
    context['application'] = Application.objects.filter(id = ap)
    if request.user.is_authenticated:
        return render(request, 'fam/viewapplication.html',context)
    else:
        return render(request, 'fam/index.html')


def acceptedapplication(request):
    context ={}
    context['user'] = request.user
    context['faculty'] = faculty.objects.all()
    context['application'] = Application.objects.filter(user = request.user.id)
    if request.user.is_authenticated:
        return render(request, 'fam/acceptedapplication.html',context)
    else:
        return render(request, 'fam/index.html')

def rejectedapplication(request):
    context ={}
    context['user'] = request.user
    context['faculty'] = faculty.objects.all()
    context['application'] = Application.objects.filter(user = request.user.id)
    if request.user.is_authenticated:
        return render(request, 'fam/rejectedapplication.html',context)
    else:
        return render(request, 'fam/index.html')

def createapplication(request):
    context ={}
    context['user'] = request.user
    context['faculty'] = faculty.objects.all()
    context['application'] = Application.objects.filter(user = request.user.id)
    if request.user.is_authenticated:
        return render(request, 'fam/createapplication.html',context)
    else:
        return render(request, 'fam/index.html')

def addapplication(request):
    context ={}
    subject = request.POST.get('subject')
    body = request.POST.get('body')
    if subject == "" or body == "":
        context['check'] = 0
    else:
        obj = Application(user = request.user, subject = subject, body = body)
        obj.save()
    
    if request.user.is_authenticated:
        return render(request, 'fam/addapplication.html',context)
    else:
        return render(request, 'fam/index.html')

def mypost(request):
    context ={}
    context['user'] = request.user
    context['faculty'] = faculty.objects.all()
    context['forum'] = Post.objects.filter(author=request.user)
    if request.user.is_authenticated:
        return render(request, 'fam/mypost.html',context)
    else:
        return render(request, 'fam/index.html')

def createpost(request):
    context ={}
    context['user'] = request.user
    context['faculty'] = faculty.objects.all()
    context['forum'] = Post.objects.filter(author=request.user)
    if request.user.is_authenticated:
        return render(request, 'fam/createpost.html',context)
    else:
        return render(request, 'fam/index.html')

def addpost(request):
    context ={}
    title = request.POST.get('title')
    body = request.POST.get('body')
    if title == "" or body == "":
        context['ch'] = 0
    else:
        obj = Post(author = request.user, title = title, body = body)
        obj.save()
    
    if request.user.is_authenticated:
        return render(request, 'fam/addpost.html',context)
    else:
        return render(request, 'fam/index.html')

def comment(request):
    context ={}
    context['user'] = request.user
    context['faculty'] = faculty.objects.all()
    post_id = request.GET.get('postid')
    context['comment'] = Comment.objects.filter(post_id=post_id)
    context['post_id'] = post_id

    if request.user.is_authenticated:
        return render(request, 'fam/comment.html',context)
    else:
        return render(request, 'fam/index.html')

def addcomment(request):
    context = {}
    comment = request.GET.get('comment')
    post_id = request.GET.get('postid') 
    context['post_id'] = post_id
    context['comment'] = Comment.objects.filter(post_id=post_id)
    post = Post.objects.get(post_id = post_id)
    if comment == "":
        pass
    else:
        obj = Comment(post_id=post, user=request.user, body=comment)
        obj.save()
    

    if request.user.is_authenticated:
        return render(request, 'fam/comment.html',context)
    else:
        return render(request, 'fam/index.html')


