from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField


# Create your models here.

class Images(models.Model):
    # image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length =30)
    description = models.TextField()
    location = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    image = CloudinaryField('image')
    
    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()
    
    class Meta:
        ordering = ['image']
        
    
    @classmethod
    def search_by_category(cls, category):
        images = Images.objects.filter(category__name__icontains=category)
        return images
   
    

class Location(models.Model):
        name = models.CharField(max_length =30)
        def __str__(self):
            return self.name

     
class Category(models.Model):
    name = models.CharField(max_length =30)
    def __str__(self):
        return self.name
    

    
    
