from django.urls import path
from . import views

urlpatterns = [
    path("",views.detection,name="detection"),
    path("",views.clearAll,name="clearAll")
    #path("detection",views.detect,name="detection")
]