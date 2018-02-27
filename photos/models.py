from django.db import models


# create model location
class Location(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

    
     #method to make test pass
    def save_location(self):
        self.save()


class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

    #method to make test pass
    def save_category(self):
        self.save()


# Create model image.
class Image(models.Model):
    Image_Description = models.TextField(null=True)
    Image_Name = models.CharField(max_length=30)
    Image = models.ImageField(upload_to = 'images/',null=True)
    Image_Location=models.ForeignKey(Location,null=True)
    Image_Category=models.ForeignKey(Category,blank=True,null=True)
    Image_date=models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.Image_Description
    # method to make save test pass
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

        
# define method that will query the db and fetch results
    @classmethod
    def search_by_category(cls,search_term):
        gallery = cls.objects.filter(Image_Name__icontains=search_term)
        return gallery

