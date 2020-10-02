from django.shortcuts import render
from publicApp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
# def register(request):
#     return render(request,'publicApp/register.html')

def login(request):
    try:
        msg = " "
        # Checking the request from form is POST or GET
        if request.method == "POST":
            email =request.POST.get('emailid')
            password=request.POST.get('passw')
            
            if tbl_login.objects.filter(email=email,password=password):
                user= tbl_login.objects.get(email=email,password=password)
                if user.type=='admin':
                    admin=tbl_login.objects.get(email=email,password=password)
                    aid=admin.id
                    request.session['adminsession']=aid
                    # finding Number of teachers , no of students  and no.of assignment and contacts
                    stud_count=tbl_student.objects.all().count()
                    teach_count=tbl_teachers.objects.all().count()
                    All_Assig=tbl_questin.objects.all().count()
                    # filltering the count of not replayed counts
                    All_msg=tbl_contact.objects.filter(rps='replay').count()
                    return render(request,'adminApp/index.html',{'stud_count':stud_count,'teach_count':teach_count,'All_Assig':All_Assig,'All_msg':All_msg})
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
                msg="!! No users found"  
    except:
        msg="An Exception occurs"
    return render(request,'publicApp/login.html',{'msg':msg})    
def home(request):
    return render(request,'publicApp/home.html')

def contact(request):
    msg=""
    try:
        if request.method=='POST':
            em=request.POST.get('email')
            na=request.POST.get('name')
            cont=request.POST.get('contactas')
            print(em)
            print(na)
            print(cont)
            conta=tbl_contact.objects.create(email=em,name=na,msg=cont)
    except:
        msg="!!An Exception occurs"
    return render(request,'publicApp/contact.html',{'msg':msg})

def about(request):
    return render(request,'publicApp/about.html')

# def handler404(request,exception):
#     return render(request, 'publicApp/500.html', status=404)

# def handler500(request):
#     return render(request, 'publicAp/500.html', status=500)