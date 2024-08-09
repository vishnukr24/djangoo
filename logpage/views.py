from django.shortcuts import render, redirect
from . models import Register
from django.contrib import messages
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
        user = Register.objects.filter(name=name, password=password).first()
        if user is None:
            messages.error(request, 'invalid password')
            return redirect('signin')
        else:
            request.session['name'] = name
            return redirect('home')
    return render(request, 'signin.html')
def logout(request):
    if 'name' in request.session:
        request.session.flush()
        return redirect('sigin')
    return redirect('home')




def viewall(request):
    if 'uname' not in request.session:
        return redirect('signin')
    reg=Register.objects.all()
    context={
        'reg':reg,
    }
    return render(request,"viewreg.html",context)
def updatereg(request,pk):
    pass
def updatedata(request,pk):
    name=request.POST["name"]
    phone=request.POST["phone"]
    email=request.POST["email"]
    username=request.POST["uname"]
    password=request.POST["password"]
    reg = Register.objects.get(id=pk)
    reg.name=name
    
    




