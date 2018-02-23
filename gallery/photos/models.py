from django.db import models


# create model location
class Location(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

# Create model image.
class Image(models.Model):
    Image_Description = models.CharField(max_length=30,null=True)
    Image_Name = models.CharField(max_length=30)
    # Image = models.CharField(max_length=30)
    Image_Location=models.ForeignKey(Location,null=True)
    Image_Category=models.ManyToManyField(Category,blank=True)
    Image_date=models.DateTimeField(auto_now_add=True,null=True)


    
    

