from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
from .forms import *
from .ObjectDetection import detect
from django.core.files.storage import FileSystemStorage
import os
from django.conf.urls.static import static
from django.conf import settings



def clearAll(request):
    return render(request,'detection/home.html')
# Create your views here.
def detection(request):
    imageUrls=[]
    fs=FileSystemStorage()
    if os.path.exists('E:/NewDjangoProjects/object detection/objectDetection/static/images/results'):
        #print("yes Images of Results exits")
        for i in range(1,11):
            resImg=fs.open(f"results/result-{i}.jpg")
            imageUrls.append(fs.url(resImg))

    else:
        for i in range(1,11):
            detect(f"{i}.jpg") 
            resImg=fs.open(f"results/result-{i}.jpg")
            imageUrls.append(fs.url(resImg))
    
    del fs
    
    return render(request,'detection/Home.html',{'form':NameForm,"Images":imageUrls[1:],"FirstImage":imageUrls[0]})
    #return render(request,'detection/Home.html',{'form':NameForm,"image":fs.url(resImg)})

