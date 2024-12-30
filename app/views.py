from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def insert_dept(request):
    Dno=int(input("Enter the deptno:"))
    Dname=input("Enter the dept name:")
    D_loc=input("Enter the location:")
    DTO=dept.objects.get_or_create(Dno=Dno,Dname=Dname,D_loc=D_loc)
    if DTO[1]:
       DTO=dept.objects.all()
       d={'DTO':DTO}
       return render(request,'display_dept.html',d)
    else:
        return HttpResponse("Dept not created")



def insert_emp(request):
    Eno=int(input("Enter the emp no:"))
    Ename=input("Enter the emp name:")
    sal=int(input("Enter the salary:"))
    job=input("Enter the designation:")
    Hiredate=input("Enter the hiredate:")
    comm= input('Enter the comm:')
    if comm:
       comm=int(comm)
    else:
        comm=None 
    Mgr=input("Enter the mgr no")
    if Mgr:
        Mgr=int(Mgr)
        Mgro=emp.objects.filter(Eno=Mgr)
        if Mgro:
            Mg=Mgro[0]
        else:
            Mg=None
      
    else:
        Mg=None
    Dno=int(input("Enter the deptno:"))
    DO=dept.objects.get(Dno=Dno)
    ETO=emp.objects.get_or_create(Eno=Eno,Ename=Ename,sal=sal,job=job,Hiredate=Hiredate,comm=comm,Mgr=Mg,Dno=DO)
    if ETO[0]:
         ETO=emp.objects.all()
         d={'ETO':ETO}
         return render(request,'display_emp.html',d)
    else:
        return HttpResponse("Emp is already present ")

def display_dept(request):
    DTO=dept.objects.all()
    d={'DTO':DTO}
    return render(request,'display_dept.html',d)

def display_emp(request):
    ETO=emp.objects.all()
    d={'ETO':ETO}
    return render(request,'display_emp.html',d)
