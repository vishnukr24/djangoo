from django.shortcuts import render, HttpResponse, render

app_name = 'home'
# Create your views here.
def index(request):
    person = {
        'name': 'Gokul',
        'age': 25,
        'city': 'Bangalore',
        }
    return render(request, 'index.html', person)


def about(request):
    return render(request,"about.html")