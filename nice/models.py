from django.db import models

# Create your models here.

class Images(models.Model):
    image = models.ImageField(upload_to='images')
    image_name = models.CharField(max_length =30)
    description = models.TextField()
    location = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    

class Location(models.Model):
   

class Category(models.Model):
   
