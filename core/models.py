from django.db import models

# Create your models here.
#images model 
class Images(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images')
    description = models.TextField()
    location = models.CharField()
    category = models.CharField()
    
    def save_image(self):
        self.save()
    
  
class Location(models.Model):
    name = models.CharField()
    description = models.TextField()
    Images = models.ForeignKey(Images,on_delete=models.CASCADE,)
    
class Category(models.Model):
    name = models.CharField()
    description = models.TextField()
    Images = models.ForeignKey(Images,on_delete=models.CASCADE,)
    
