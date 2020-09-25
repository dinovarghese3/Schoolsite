"""schoolSit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from publicApp.views import *
from adminApp.views import *
from studentApp.views import *
from teacherApp.views import *
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # publicApp
    url('home/$',home,name='home'),
    url('login/$',login,name='login'),
    # url('registr/$',register,name='register'),
    url('contact/$',contact,name='contact'),
    url('about/$',about,name='about'),
    #adminApp
    url('allstudents/$',allstudents,name='allstudents'),
    url('allteachers/$',allteachers,name='allteachers'),
    url('messages/$',mesage,name='mesage'),
    url('registerTe/$',registerteacher,name='registerteacher'),
    url('index/$',index,name='index'),
    url('logout/$',logout,name='logout'),
    #teacherApp
    url('teacherprofile/$',t_profile,name='t_profile'),
    url('Students/$',students,name='students'),
    url('studentregister',registerstud,name='registerstud'),
    url('addAssignment',addassignment,name='addassignment'),
    url('viewAssignments',viewassi,name='viewassi'),
    url(r'^responds/(?P<id>[0-9]+)$',responds,name='responds'),
    url(r'^viewfile/(?P<id>[0-9]+)$',viewfile,name='viewfile'),
    url(r'^summaryfind/(?P<id>[0-9]+)$',summaryfind,name='summaryfind'),
    #studentApp
    url('studprof/$',stud_profile,name='stud_profile'),
    url(r'^answer/(?P<id>[0-9]+)$',answer,name='answer'),
    url('allassignments/$',allassignments,name='allassignments'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
