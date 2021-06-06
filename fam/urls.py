from django.contrib.auth import views as auth_views
from django.urls import path,include
from . import views

app_main = 'fam'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_request, name='login_request'),
    path('home/',views.home, name='home'),
    path('logout/', views.logout_request, name='logout_request'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('subject/', views.subject, name='subject'),
    path('publication/', views.publication, name='publication'),
    path('education/', views.education, name='education'),
    path('projects/', views.projects, name='projects'),
    path('achievement/', views.achievement, name='achievement'),
    path('attendance/', views.attendance, name='attendance'),
    path('forum/', views.forum, name='forum'),
    path('schedule/', views.schedules, name='schedules'),
    path('application/', views.application, name='application'),
    path('acceptedapplication/', views.acceptedapplication, name='acceptedapplication'),
    path('rejectedapplication/', views.rejectedapplication, name='rejectedapplication'),
    path('createapplication/', views.createapplication, name='createapplication'),
    path('addapplication/', views.addapplication, name='addapplication'),
    path('mypost/', views.mypost, name='mypost'),
    path('createpost/', views.createpost, name='createpost'),
    path('addpost/', views.addpost, name='addpost'),
    path('comment/', views.comment, name='comment'),
    path('addcomment/', views.addcomment, name='addcomment'),
    


    







    path('viewapplication/', views.viewapplication, name='viewapplication'),

    path('accounts/', include('django.contrib.auth.urls')),

]