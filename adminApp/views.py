from django.shortcuts import render

from publicApp.models import *
# Create your views here.
def allstudents(request):
    students=tbl_student.objects.all()
    return render(request,'adminApp/AllStudents.html',{'students':students})

def allteachers(request):
    
    teacher=tbl_teachers.objects.all()
    return render(request,'adminApp/AllTeachers.html',{'teacher':teacher})

def mainpage(request):
    return render(request,'adminApp/mainpage.html')

def mesage(request):
    return render(request,'adminApp/msgs.html')

def registerteacher(request):
    if request.method == 'POST':
        fn=request.POST.get('fname')
        sn=request.POST.get('lname')
        ga=request.POST.get('age')
        da=request.POST.get('dob')
        num=request.POST.get('ph')
        add=request.POST.get('address')
        em=request.POST.get('mail')
        cl=request.POST.get('class')
        div=request.POST.get('division')
        imag=request.FILES['img']
        pas=request.POST.get('pasw')
        gen=request.POST.get('gender')
        teacherdata=tbl_teachers.objects.create(Fname=fn,Lname=sn,Age=ga,dob=da,address=add,phonenumber=num,clas=cl,division=div,dp=imag,type="teacher",email=em,password=pas,gender=gen)
        tlog=tbl_login.objects.create(email=em,password=pas,type='teacher')
    return render(request,'adminApp/registerTea.html')

def index(request):
    return render(request,'adminApp/index.html')

def logout(request):
    teacher=request.session.flush()
    return render(request,'publicApp/home.html')