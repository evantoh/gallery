from django.test import TestCase
from .models import Image,Category,Location

#create test for image class
class imageTestClass(TestCase):
    # set up method
    def setUp(self):
        self.image=Image(Image_Description = 'the beaty nature',
        Image_Name='travel')

        # testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

# testing save method for image
    def test_save_method(self):
        self.image.save_image()
        images= Image.objects.all()
        self.assertTrue(len(images)> 0)

# testing delete image
    # def test_delete_image(self):
    #     self.image=Image(Image_Description = 'the beaty nature',
    #     Image_Name='travel')

    #     self.image.delete_image()
    #     images= Image.objects.all()
    #     self.assertTrue(len(images)< 1)

class categoryTestClass(TestCase):

        
    #testing save method for class category
    def test_save_method(self):
        self.category.save_category()
        images= Category.objects.all()
        self.assertTrue(len(images)> 0)


