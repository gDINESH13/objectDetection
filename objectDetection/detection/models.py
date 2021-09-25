from django.db import models

# Create your models here.

class detectionHistory(models.Model):
    rawImage=models.FileField(null=True,blank=True)
    resImage=models.FileField(null=True,blank=True)
    