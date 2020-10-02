from django.shortcuts import render
from publicApp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

# Create your views here.
def t_profile(request):
    tid=request.session['teacherid']
    data=tbl_teachers.objects.get(id=tid)    
    return render(request,'teacherApp/t_profile.html',{'data':data})

def students(request):
    try:
        t=request.session['teacherid']
        d=tbl_teachers.objects.get(id=t)
        cl=d.clas
        div=d.division
        stud=tbl_student.objects.filter(clas=cl,division=div)
    except:
        return render(request,'publicApp/404.html')
    return render(request,'teacherApp/AllStudents.html',{'stud':stud})

def registerstud(request):
    try:
        if request.method == 'POST':
            Fn=request.POST.get('fname')
            Ln=request.POST.get('ln')
            adnu=request.POST.get('adno')
            ag=request.POST.get('age')
            db=request.POST.get('dob')
            ad=request.POST.get('address')
            ph=request.POST.get('ph')
            email=request.POST.get('mail')
            gen=request.POST.get('gender')
            im=request.FILES["photo"]
            pas=request.POST.get('pass')
            t=request.session['teacherid']
            d=tbl_teachers.objects.get(id=t)
            cl=d.clas
            div=d.division
            stud=tbl_student.objects.create(Fname=Fn,Lname=Ln,admisionno=adnu,Age=ag,dob=db,address=ad,phonenumber=ph,email=email,clas=cl,division=div,dp=im,type="student",password=pas,gender=gen)
            log=tbl_login.objects.create(email=email,password=pas,type='student')
    except:
            return render(request,'publicApp/404.html')
    return render(request,'teacherApp/addStudent.html')

def addassignment(request):
    try:
        t=request.session['teacherid']
        data=tbl_teachers.objects.get(id=t)
        e=data.email
        c=data.clas
        d=data.division
        if request.method =='POST':
            qe=request.POST.get('ques')
            l=request.POST.get('ld')
            Assignments=tbl_questin.objects.create(email=e,clas=c,division=d,questin=qe,ldate=l)
    except:
        return render(request,'publicApp/404.html')
    return render(request,'teacherApp/addAssignmentQ.html',{'data':data})

def viewassi(request):
    try:
        t=request.session['teacherid']
        data=tbl_teachers.objects.get(id=t)
        qdata=tbl_questin.objects.filter(clas=data.clas,division=data.division)
    except:
        return render(request,'publicApp/404.html')
    return render(request,'teacherApp/viewAllAssignment.html',{'qdata':qdata})

def responds(request,id):
    try:
        answer=tbl_answers.objects.filter(qid=id)
        qesid=id
        # Notsubmit=Allsubmision(qesid)
        
        tid=request.session['teacherid']
        data1=tbl_teachers.objects.get(id=tid)
        cl=data1.clas
        di=data1.division
        intrerlist=[]
        data=tbl_student.objects.filter(clas=cl,division=di)
        for i in data:
            if tbl_answers.objects.filter(email=i.email):
                continue
            else:
                intrerlist.append(i)
    except:
        return render(request,'publicApp/404.html')
    return render(request,'teacherApp/responds.html',{'answer':answer,'qesid':qesid,'intrerlist':intrerlist})

def viewfile(request,id):
    try:
        fileop=tbl_answers.objects.get(id)
    except:
        return render(request,'publicApp/404.html')
    return render(request,'teacherApp/viewfilecontent.html',{'fileop':fileop})

def summaryfind(request,id):
    try:

        import nltk 
        from nltk.corpus import stopwords 
        from nltk.tokenize import word_tokenize, sent_tokenize 
        
        # Input text - to summarize 
        # # text="NULL"
        # print('--------------------------')
        # print(id)
        # print('--------------------------')
        data=tbl_answers.objects.get(id=id)
        path="./"+data.answes.url
        # print(file)
        # f=tb.answes.url
        with open(path,'r') as file:
            text = file.read()
        # text =  request.POST.get('link')
        if text == "NULL":
            summary="error"
        else:
            # Tokenizing the text 
            stopWords = set(stopwords.words("english")) 
            words = word_tokenize(text) 
            # Creating a frequency table to keep the  
            # score of each word 
            freqTable = dict() 
            for word in words: 
                word = word.lower() 
                if word in stopWords: 
                    continue
                if word in freqTable: 
                    freqTable[word] += 1
                else: 
                    freqTable[word] = 1
            # Creating a dictionary to keep the score 
            # of each sentence 
            sentences = sent_tokenize(text) 
            sentenceValue = dict() 
            for sentence in sentences: 
                for word, freq in freqTable.items(): 
                    if word in sentence.lower(): 
                        if sentence in sentenceValue: 
                            sentenceValue[sentence] += freq 
                        else: 
                            sentenceValue[sentence] = freq 
            sumValues = 0
            for sentence in sentenceValue: 
                sumValues += sentenceValue[sentence] 
            # Average value of a sentence from the original text 
            average = int(sumValues / len(sentenceValue)) 
            # Storing sentences into our summary. 
            summary = '' 
            for sentence in sentences: 
                if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)): 
                    summary += " " + sentence 
            # print(summary)  
            data=summary
    except:
        return render(request,'publicApp/404.html')    
    return render(request,"teacherApp/viewfilecontent.html",{'data':data})
def message(request,id):
    try:

        stud=tbl_student.objects.get(admisionno=id)
        studmess=tbl_message.objects.filter(rid=stud.email)
        em=stud.email
        
        tid=request.session['teacherid']
        data=tbl_teachers.objects.get(id=tid) 
        # messages=tbl_message.objects.filter(email=em)
        # mess=tbl_message.objects.filter(rid=data.email)
        # item=zip(mess,studmess)
        if request.method=='POST':
            anws=request.POST.get('msg')
            mess=tbl_message.objects.create(email=data.email,message=anws,rid=stud.email)
            return HttpResponseRedirect(reverse('students'))
    except:
        return render(request,'publicApp/404.html')
    return render(request,'teacherApp/message.html',{'studmess':studmess,'stud':stud,'data':data})
# def Allsubmision(request,id):
    allsubmission=tbl_answers.objects.filter(qid=id)
    tid=request.session['teacherid']
    data1=tbl_teachers.objects.get(id=tid)
    cl=data1.clas
    di=data1.division
    # stud=tbl_student.objects.filter(clas=cl,division=di)
    # studlist=[]
    # for i in stud:
    #     studlist.append(i.admisionno)
    # submited=[]
    # for j in allsubmission:
    #     submited.append(j.adno)
    # studentset=set(studlist)
    # submitedset=set(submited)
    # ----------------------------
    # intrerlist=[]
    # data=tbl_student.objects.filter(clas=cl,division=di)
    # for i in data:
    #     if tbl_answers.objects.filter(email=i.email):
    #         continue
    #     else:
    #         intrerlist.append(i)

    # intersec=studentset.difference(submitedset)
    # print(intersec)
    # interlist=list(intersec)
    return ({'intrerlist':intrerlist})
def Assignmentfile(request,id):
    try:
        data=tbl_answers.objects.get(id=id)
        path="./"+data.answes.url
        with open(path,'r') as file:
            text = file.read()
        if request.method=='POST':
            mr=request.POST.get('mark')
            data.mark=mr
            data.save()
    except:
        return render(request,'publicApp/404.html')
    return render(request,'teacherApp/assignmentcontent.html',{'text':text,'data':data})
# def printdoc(request,id):
#     t=request.session['teacherid']
#     d=tbl_teachers.objects.get(id=t)
#     cl=d.clas
#     file=tbl_answers.objects.filter(qid=id,clas=cl,division=d)
#     contet={'file':file}
#     print(contet)
#     # Create a file-like buffer to receive PDF data.
#     buffer = io.BytesIO()

#     # Create the PDF object, using the buffer as its "file."
#     p = canvas.Canvas(buffer)

#     # Draw things on the PDF. Here's where the PDF generation happens.
#     # See the ReportLab documentation for the full list of functionality.
#     p.drawString(100, 100,'file')

#     # Close the PDF object cleanly, and we're done.
#     p.showPage()
#     p.save()

#     # FileResponse sets the Content-Disposition header so that browsers
#     # present the option to save the file.
#     buffer.seek(0)
#     return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
    
