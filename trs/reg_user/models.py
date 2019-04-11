from django.db import models

# Create your models here.
class User_detail(models.Model):
    name= models.CharField(max_length=200)
    email=models.EmailField(max_length=200,primary_key=True)
class place(models.Model):
    name=models.CharField(max_length=200,primary_key=True)
    desc=models.CharField(max_length=2000)
    img=models.CharField(max_length=200)