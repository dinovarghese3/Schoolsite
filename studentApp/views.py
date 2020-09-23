from django.shortcuts import render
from publicApp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from datetime import date
# Create your views here.
def stud_profile(request):
    sid=request.session['studid']
    data=tbl_student.objects.get(admisionno=sid)
    return render(request,'studentApp/studeprof.html',{'data':data})

def answer(request,id):
    asi=tbl_questin.objects.get(id=id)
    qid=asi.id
    sid=request.session['studid']
    data=tbl_student.objects.get(admisionno=sid)
    em=data.email
    cl=data.clas
    today = date.today()
    d1 = today.strftime("%Y/%m/%d")
    divi=data.division
    admi=data.admisionno
    if request.method=='POST':
        anws=request.FILES['an']
        anwersub=tbl_answers.objects.create(name=data.Fname+data.Lname,adno=admi,qid=qid,email=em,clas=cl,division=divi,answes=anws,sdate=d1)
        return HttpResponseRedirect(reverse('allassignments'))    
    return render(request,'studentApp/answer.html',{'asi':asi})
def allassignments(request):
    sid=request.session['studid']
    data=tbl_student.objects.get(admisionno=sid)
    questin=tbl_questin.objects.filter(clas=data.clas,division=data.division)
    return render(request,'studentApp/allAssignmentq.html',{'questin':questin})