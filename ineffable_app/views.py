from django.shortcuts import render,redirect,reverse
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse,HttpResponseRedirect
from .models import AdminLogin,ResgisterStudent
from django.core.exceptions import ObjectDoesNotExist
from xhtml2pdf import pisa
from django.template.loader import get_template
from io import BytesIO
from ineffable_app.models import CentreRegisterStudent,Status_create,Studentform,Add_Centres,Add_Students,CentreStatus,Student_form_creation
from django.contrib.auth.decorators import login_required 
import pandas as pd
import sqlite3
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.db import connection

# Create your views here.
def home(request):
    if request.method=='GET':
        resp=render(request,'index.html')    
        return resp
    elif request.method=="POST":
        if 'btnenq' in request.POST:
            resp=render(request,'enquiry.html')    
            return resp
        elif 'btnlog' in request.POST:
            resp=render(request,'adminAPP/index.html')    
            return resp    
        elif "btncenter" in request.POST:
              user=User.objects.all()
              resp=render(request,"adminAPP/search_centre.html",{'user':user})
              return resp
  
def about(request):    
    data=ResgisterStudent.objects.all()
    for a in data:
         print(a.first_name)
    if request.method=='GET':
            resp=render(request,'about.html') 
            return resp
    elif request.method=="POST":
            if 'btnenq' in request.POST:
                resp=render(request,'enquiry.html')    
                return resp
            elif 'btnlog' in request.POST:
                resp=render(request,'adminAPP/index.html')    
                return resp 
            elif "btncenter" in request.POST:
                user=User.objects.all()
                resp=render(request,"adminAPP/search_centre.html",{'user':user})
                return resp 

def notice(request):    
        if request.method=='GET':
            resp=render(request,'notice.html') 
            return resp
        elif request.method=="POST":
            if 'btnenq' in request.POST:
                 resp=render(request,'enquiry.html')    
                 return resp
            elif 'btnlog' in request.POST:
                 resp=render(request,'adminAPP/index.html')    
                 return resp  

def contact(request):    
        if request.method=='GET':
            resp=render(request,'contact.html') 
            return resp
        elif request.method=="POST":
              if 'btnenq' in request.POST:
                 resp=render(request,'enquiry.html')    
                 return resp
              elif 'btnlog' in request.POST:
                  resp=render(request,'adminAPP/index.html')    
                  return resp    
              elif "btncenter" in request.POST:
               user=User.objects.all()
               resp=render(request,"adminAPP/search_centre.html",{'user':user})
               return resp
  
          #   if 'btnenq' in request.POST:
          #        resp=render(request,'enquiry.html')    
          #        return resp
          #   elif 'btnlog' in request.POST:
          #        resp=render(request,'adminAPP/index.html')    
          #        return resp  


# def enq_form(request):
#    try: 
#     srn=int(request.POST.get("txtrn",0))
#     data=Add_Students.objects.filter(rollno=srn).all()
#     data2=Status_create.objects.get(student_rollno=srn)
#     stas=data2.status
#     d1={'data':data,'status':stas}
#     resp=render(request,"enquiry.html",context=d1)
#     return resp
#    except ObjectDoesNotExist:
#         d={'msg':"not found at"}
#         resp=render(request,"error.html",context=d)
#         return resp
def search(request):
     return render(request,"adminAPP/search.html")
def searchcentre(request):
     if request.method=="GET":
          return render(request,"adminAPP/search.html")
     elif request.method=="POST":
          #centrecode=int(request.POST.get('centrecode',00))
          if "btn_submit" in request.POST:
                    centrecode=int(request.POST.get('centrecode',00))
                    data=Add_Centres.objects.filter(centrecode=centrecode).all()
                    data1=Add_Students.objects.filter(centre_code=centrecode).all()
                    d1={'data':data,'data1':data1} 
                    #print(data)
                    resp=render(request,'adminAPP/search.html',context=d1)
                    return resp      
          

def login_centre(request):
     return render(request,"adminAPP/sample.html")        


# def centre_logout(request):
#      logout(request)
#      return redirect('')

# def add_student(request):
#      return render(request,"adminApp/Student_Register_form.html")


def sample(request):
     return render(request,"adminAPP/sample.html")

# center login
def  centre_login(request):
     if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            d={'user':user}
            return render(request,"adminAPP/form_centre.html",context=d)
     return render(request,"adminAPP/centre_login.html")

def centre_logout(request):
     logout(request)
     return redirect('')

def courses(request):    
        if request.method=='GET':
            resp=render(request,'course.html') 
            return resp
        elif request.method=="POST":
              if 'btnenq' in request.POST:
                 resp=render(request,'enquiry.html')    
                 return resp
              elif 'btnlog' in request.POST:
                  resp=render(request,'adminAPP/index.html')    
                  return resp    
              elif "btncenter" in request.POST:
               user=User.objects.all()
               resp=render(request,"adminAPP/search_centre.html",{'user':user})
               return resp
  

# def adduser(request):
#      if request.method=="POST":
#           if 'btnuser' in request.POST:
#                res=render(request,'adminAPP/registration.html')
#                return res
#           elif 'btnlogout' in request.POST:
#             res=render(request,'index.html')
#             return res

def index(request):
    resp=render(request,"adminAPP/index.html")
    return resp

def hello(request):
    resp=render(request,"adminAPP/hello.html")
    return resp

def centrelogin(request):
     if request.method == 'POST':
            username=request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                  auth.login(request,user) 
                  dt=user.username
               #    print(dt)
                  data=Add_Centres.objects.get(Centrecode=dt)
                  d1=data.Centrename
                  print(d1)
                  data2=Add_Students.objects.filter(Centrename='2:Struggle Computer Institute')
                  for d in data2:
                        print(d.Studentname)
               #    for i in data2:
               #          print(i.Centrename,i.Studentname)
               #    sql="select * from ineffable_app_add_students where Centrename='{d1}' "
               #    for d in  Add_Students.objects.raw(sql):
               #      print(d.Studentname)
               #      print(d.Fathername)
               #      print(d.Mothername)
               #      print(d.Centrecode)
               #      print(d.Centrename)
               #      print(d.rollno)
               #    if Add_Students.objects.filter(Centrename='2:Struggle Computer Institute').exists():
                        
               #    x = Add_Centres.objects.get(centrecode=809)
               #    print(x.centrecode)
               #    y=Add_Students.objects.filter(centre_code=809)
               #    print(y)
               #    sql="select * from ineffable_app_add_students  where Centre_code='dt' "
               #    cursor=connection.cursor()
               #    exe=cursor.execute(sql)
               #    print(exe)
                  d={'username':username,'data2':data}
                  return render(request,"adminAPP/loggedin.html",context=d)
            else:
                   return HttpResponse("<h1>not founding</h1>")
     else:
         return render(request,'adminAPP/sample.html')
