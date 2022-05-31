from django.db import models



class Client (models.Model):
    fullname = models.CharField(max_length=100)
    secondname =models.CharField(max_length=100)
    adresse =models.CharField(max_length=50)
    email =models.CharField(max_length=50)
    ville =models.CharField(max_length=50)
    pays =models.CharField(max_length=50)
    

# Create your models here.
