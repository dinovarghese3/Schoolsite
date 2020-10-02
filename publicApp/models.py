from django.db import models

# Create your models here.
class tbl_login(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=10)

class tbl_teachers(models.Model):
    Fname=models.CharField(max_length=20)
    Lname=models.CharField(max_length=20)
    Age=models.IntegerField()
    dob=models.DateField(max_length=20)
    address=models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    email=models.CharField(max_length=30,default="......")
    clas=models.IntegerField()
    division=models.CharField(max_length=5)
    dp=models.FileField(upload_to='images',verbose_name='file',null=True,blank=True)
    type=models.CharField(max_length=10)
    password=models.CharField(max_length=30,default=123)
    gender=models.CharField(max_length=10,default="none")

class tbl_student(models.Model):
    Fname=models.CharField(max_length=20)
    Lname=models.CharField(max_length=20)
    admisionno=models.IntegerField(default="lastname",primary_key=True)
    Age=models.IntegerField()
    dob=models.DateField(max_length=20)
    address=models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    email=models.CharField(max_length=30,default="......")
    clas=models.IntegerField()
    division=models.CharField(max_length=5)
    dp=models.FileField(upload_to='stud_images',verbose_name='file',null=True,blank=True)
    type=models.CharField(max_length=5)
    password=models.CharField(max_length=30,default=123)
    gender=models.CharField(max_length=10,default="none")

class tbl_questin(models.Model):
    email=models.CharField(max_length=30)
    clas=models.IntegerField()
    division=models.CharField(max_length=5)
    questin=models.CharField(max_length=200)
    ldate=models.CharField(max_length=20)

class tbl_answers(models.Model):
    name=models.CharField(max_length=50)
    adno=models.IntegerField()
    email=models.CharField(max_length=30)
    clas=models.IntegerField()
    division=models.CharField(max_length=5)
    qid=models.CharField(max_length=50)
    sdate=models.CharField(max_length=20)
    mark=models.IntegerField(default=0)
    answes=models.FileField(upload_to='answers',verbose_name='file',null=True,blank=True)
class tbl_message(models.Model):
    message=models.CharField(max_length=200)
    email=models.CharField(max_length=20)
    rid=models.CharField(max_length=20)

class tbl_contact(models.Model):
    msg=models.CharField(max_length=200)
    email=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    rps=models.CharField(max_length=10,default="replay")
