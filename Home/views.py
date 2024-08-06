from django.shortcuts import render, HttpResponse, render
from . models import department, Doctor
app_name = 'home'
# Create your views here.
def index(request):
    nums = range(0,10)
    person = {
        'name': 'Gokul',
        'age': 26,
        'city': 'Bangalore',
        'nums':nums,
        }    
    return render(request, 'index.html', person)


def about(request):
    return render(request,"about.html")


def show(request):
    number ={
        'nums':[1,2,3,4,5,6,7,8,9,10]
    }
    return render (request, 'show.html', number)


def demo(request):
    return render (request, 'demo.html')



def dept(request):
    dic_dept = {
        'dept':department.objects.all()
    }
    return render (request, 'departments.html', dic_dept)


def doctor(request):
    doctor = {
        'doctor':Doctor.objects.all()
    }
    return render (request, 'doctor.html', doctor)


def booking(request):
    doctor = {
        'doctor':Doctor.objects.all()
    }
    return render (request, 'doctor.html', doctor)