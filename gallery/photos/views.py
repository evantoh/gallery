
from django .shortcuts import render
from .models import Image,Location,Category 


# Create your views here.
def welcome(request):
    images =Image.objects.all()
    arg ={ "images":images}
    return render(request,'photos/welcome.html',arg)