from django.db import models

# Create your models here.
class Register(models.Model):
   name=models.CharField(max_length=100)
   phone=models.CharField(max_length=20)
   email=models.EmailField()
   username=models.CharField(max_length=90)
   password=models.CharField(max_length=50)    
class Login(models.Model):
   username=models.CharField(max_length=90)
   password=models.CharField(max_length=50)    