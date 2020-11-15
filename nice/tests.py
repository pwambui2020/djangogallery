from django.test import TestCase
from .models import Images,Category,Location

# Create your tests here.
class ImagesTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.image = Images(image='image', image_name='', description='', location='', category='')
        
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Images))