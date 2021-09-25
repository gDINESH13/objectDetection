from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
from .forms import *
from .ObjectDetection import detect
from django.core.files.storage import FileSystemStorage

def clearAll(request):
    return render(request,'detection/home.html')
# Create your views here.
def detection(request):
    
    if request.method=="POST":
        form=NameForm(request.POST,request.FILES)
        if form.is_valid():
            # print(form.cleaned_data['docFile'])
            # img=detectionHistory(rawImage=form.cleaned_data['docFile'])
            # img.save()
            # print(img.rawImage.url)
            image=form.cleaned_data['docFile']
            fs=FileSystemStorage()
            filePath=fs.save(image.name,image)
            fileName=fs.url(filePath)
            file=[fileName,image.name]
            detect(file)
            resImg=fs.open(f"result-{image.name}")
            resFilePath=fs.url(resImg)
            return render(request,'detection/home.html',{'filePath':resFilePath,'form':NameForm})
        return HttpResponseRedirect(reverse('detection'))
    
    else:
        
        return render(request,'detection/Home.html',{'form':NameForm,})

