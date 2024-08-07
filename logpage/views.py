from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import RegisterForm
from . models import Register
# Create your views here.
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['pass']
        cpass = request.POST['cpass']
        myreg=Register(name=name, phone=phone, email=email, password=password, confirm_password=cpass)
        myreg.save()
        return redirect('signin')
    return render(request, 'register.html')
        

def signin(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['pass']
        user = Register.objects.get(name=name, password=password)
        if user is None:
            messages.error(request, 'invalid password')
            return redirect('signin')
        else:
            request.session['name'] = name
            return redirect('home')
    return render(request, 'signin.html')