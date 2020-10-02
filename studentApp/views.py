from django.shortcuts import render
from publicApp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from datetime import date
# Create your views here.
def stud_profile(request):
    # Creating a session with the session name 'studid'
    sid=request.session['studid']
    data=tbl_student.objects.get(admisionno=sid)
    return render(request,'studentApp/studeprof.html',{'data':data})

def answer(request,id):
    try:
        # Getting the questin details with the id
        asi=tbl_questin.objects.get(id=id)
        qid=asi.id
        sid=request.session['studid']
        data=tbl_student.objects.get(admisionno=sid)
        em=data.email
        cl=data.clas
        divi=data.division
        admi=data.admisionno

        # Assignment submission data
        today = date.today()
        d1 = today.strftime("%Y/%m/%d")
        
        if request.method=='POST':
            anws=request.FILES['an']
            if tbl_answers.objects.filter(email=em,qid=qid):
                print("All ready ")
            else:
                anwersub=tbl_answers.objects.create(name=data.Fname+data.Lname,adno=admi,qid=qid,email=em,clas=cl,division=divi,answes=anws,sdate=d1)
            return HttpResponseRedirect(reverse('allassignments')) 
    except:
        # If any error occurs in submiting file
        return render(request,'publicApp/404.html')   
    return render(request,'studentApp/answer.html',{'asi':asi})
def allassignments(request):
    try:
        sid=request.session['studid']
        data=tbl_student.objects.get(admisionno=sid)
        # filltering the questins with the class and division
        questin=tbl_questin.objects.filter(clas=data.clas,division=data.division)
    except:
        return render(request,'publicApp/404.html')  
    return render(request,'studentApp/allAssignmentq.html',{'questin':questin})
def teacherprofile(request):
    try:
            
        sid=request.session['studid']
        data=tbl_student.objects.get(admisionno=sid)
        cl=data.clas
        d=data.division
        teacher=tbl_teachers.objects.get(clas=cl,division=d)
    except:
        return render(request,'publicApp/404.html')
    return render(request,'studentApp/teprofileview.html',{'teacher':teacher})


def studmessage(request,id):
    try:
        # Getting Teacher details with the id 

        teac=tbl_teachers.objects.get(id=id)
        em=teac.email

        # Getting student details

        sid=request.session['studid']
        data=tbl_student.objects.get(admisionno=sid)

        # Getting messages from the databse with reciverid= studentid....Always the student is the reciver

        messages=tbl_message.objects.filter(rid=data.email)

        # mess=tbl_message.objects.filter(email=em,rid=data.email)
        
        if request.method=='POST':
            anws=request.POST.get('msg')
            anwersub=tbl_message.objects.create(message=anws,rid=data.email)
            return HttpResponseRedirect(reverse('teacherprofile'))
    except:
        return render(request,'publicApp/404.html')
    return render(request,'studentApp/message.html',{'messages':messages,'teac':teac,'em':em})

