from django.shortcuts import render
from publicApp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def t_profile(request):
    tid=request.session['teacherid']
    data=tbl_teachers.objects.get(id=tid)    
    return render(request,'teacherApp/t_profile.html',{'data':data})

def students(request):
    t=request.session['teacherid']
    d=tbl_teachers.objects.get(id=t)
    cl=d.clas
    div=d.division
    stud=tbl_student.objects.filter(clas=cl,division=div)
    return render(request,'teacherApp/AllStudents.html',{'stud':stud})

def registerstud(request):
    if request.method == 'POST':
        Fn=request.POST.get('fname')
        Ln=request.POST.get('lname')
        adnu=request.POST.get('adno')
        ag=request.POST.get('age')
        db=request.POST.get('dob')
        ad=request.POST.get('address')
        ph=request.POST.get('ph')
        email=request.POST.get('mail')
        gen=request.POST.get('gender')
        im=request.FILES['photo']
        pas=request.POST.get('pass')
        t=request.session['teacherid']
        d=tbl_teachers.objects.get(id=t)
        cl=d.clas
        div=d.division
        stud=tbl_student.objects.create(Fname=Fn,Lname=Ln,admisionno=adnu,Age=ag,dob=db,address=ad,phonenumber=ph,email=email,clas=cl,division=div,dp=im,type="student",password=pas,gender=gen)
        log=tbl_login.objects.create(email=email,password=pas,type='student')
    return render(request,'teacherApp/addStudent.html')

def addassignment(request):
    t=request.session['teacherid']
    data=tbl_teachers.objects.get(id=t)
    e=data.email
    c=data.clas
    d=data.division
    if request.method =='POST':
        qe=request.POST.get('ques')
        l=request.POST.get('ld')
        Assignments=tbl_questin.objects.create(email=e,clas=c,division=d,questin=qe,ldate=l)
    return render(request,'teacherApp/addAssignmentQ.html',{'data':data})

def viewassi(request):
    t=request.session['teacherid']
    data=tbl_teachers.objects.get(id=t)
    qdata=tbl_questin.objects.filter(clas=data.clas,division=data.division)
    
    return render(request,'teacherApp/viewAllAssignment.html',{'qdata':qdata})

def responds(request,id):
    
    
    answer=tbl_answers.objects.filter(qid=id)
    return render(request,'teacherApp/responds.html',{'answer':answer})

def viewfile(request,id):
    fileop=tbl_answers.objects.get(id)
    return render(request,'teacherApp/viewfilecontent.html',{'fileop':fileop})

def summaryfind(request,id):

    import nltk 
    from nltk.corpus import stopwords 
    from nltk.tokenize import word_tokenize, sent_tokenize 
    
    # Input text - to summarize 
    # text="NULL"
    print('--------------------------')
    print(id)
    print('--------------------------')
    data=tbl_answers.objects.get(id=id)
    path="../"
    # print(file)
    # # f=tb.answes.url
    # with open('tb.answes.url','r') as file:
    #     text = file.read()
    # # text =  request.POST.get('link')
    # if text == "NULL":
    #     summary="error"
    # else:
    #     # Tokenizing the text 
    #     stopWords = set(stopwords.words("english")) 
    #     words = word_tokenize(text) 
    #     # Creating a frequency table to keep the  
    #     # score of each word 
    #     freqTable = dict() 
    #     for word in words: 
    #         word = word.lower() 
    #         if word in stopWords: 
    #             continue
    #         if word in freqTable: 
    #             freqTable[word] += 1
    #         else: 
    #             freqTable[word] = 1
    #     # Creating a dictionary to keep the score 
    #     # of each sentence 
    #     sentences = sent_tokenize(text) 
    #     sentenceValue = dict() 
    #     for sentence in sentences: 
    #         for word, freq in freqTable.items(): 
    #             if word in sentence.lower(): 
    #                 if sentence in sentenceValue: 
    #                     sentenceValue[sentence] += freq 
    #                 else: 
    #                     sentenceValue[sentence] = freq 
    #     sumValues = 0
    #     for sentence in sentenceValue: 
    #         sumValues += sentenceValue[sentence] 
    #     # Average value of a sentence from the original text 
    #     average = int(sumValues / len(sentenceValue)) 
    #     # Storing sentences into our summary. 
    #     summary = '' 
    #     for sentence in sentences: 
    #         if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)): 
    #             summary += " " + sentence 
    #     print(summary)  
    #     data=summary
    return render(request,"teacherApp/viewfilecontent.html",{'data':data})
