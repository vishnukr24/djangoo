from django.shortcuts import render
from . models import ImageGallery
from . forms import ImageForm
# Create your views here.
def image(request):
    if request.method == 'POST':
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImageForm()
    images = ImageGallery.objects.all()
    dic_form={
        'form':form,
        'images':images
    }
    return render(request, 'imagegallary.html', dic_form)

    

    

