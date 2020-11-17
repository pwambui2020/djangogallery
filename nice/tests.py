from django.test import TestCase
from .models import Images,Category,Location

# Create your tests here.
class ImagesTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.image = Images(image='image', image_name='', description='', location='', category='')
        
    def save_image(self):
        self.save()
    
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Images))
        
# Testing Save Method
    def test_save_method(self):
        self.image.save_image()
        images = Images.objects.all()
        self.assertTrue(len(images) > 0)