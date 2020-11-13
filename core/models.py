from django.db import models

# Create your models here.
#images model 
class Images(models.Model):
    
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='cars')
    description = models.TextField()
    location = models.CharField()
    category = models.CharField()
    
  
