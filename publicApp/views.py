from django.shortcuts import render
from publicApp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def register(request):
    return render(request,'publicApp/register.html')

def login(request):
    msg = " "
    if request.method == "POST":
        email =request.POST.get('emailid')
        password=request.POST.get('passw')
        if tbl_login.objects.filter(email=email,password=password):
            user= tbl_login.objects.get(email=email,password=password)
            if user.type=='admin':
                admin=tbl_login.objects.get(email=email,password=password)
                aid=admin.id
                request.session['adminsession']=aid
                return render(request,'adminApp/index.html')
            elif user.type=='teacher':
                teacher=tbl_teachers.objects.get(email=email,password=password)
                i=teacher.id
                request.session['teacherid']=i
                return HttpResponseRedirect(reverse('t_profile'))
            elif user.type=='student':
                stu=tbl_student.objects.get(email=email,password=password)
                i=stu.admisionno
                request.session['studid']=i
                return HttpResponseRedirect(reverse('stud_profile'))
        else:
            msg =" no data"
    else:
        msg=" no post"    
    return render(request,'publicApp/login.html',{'msg':msg})

def home(request):
    return render(request,'publicApp/home.html')

def contact(request):
    return render(request,'publicApp/contact.html')

def about(request):
    return render(request,'publicApp/about.html')