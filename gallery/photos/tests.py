from django.test import TestCase
from .models import Image,Category,Location

#create test for image class

class imageTestClass(TestCase):
    # set up method
    def setUp(self):
        self.image=Image(Image_Description = 'the beaty nature',Image_Name='travel')

        # testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

# testing save method
    def test_save_method(self):
        self.image.save_image()
        images= Image.objects.all()
        self.assertTrue(len(images)> 0)
