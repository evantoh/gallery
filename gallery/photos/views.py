
from django .shortcuts import render
from .models import Image,Location,Category 


# Create your views here.
def welcome(request):
    #get objects from the databasei.e from class image
    images =Image.objects.all()
    #pass the objects to view
    return render(request,'photos/welcome.html',{ "images":images})

def search_results(request):
    if 'Image' in request.GET and request.GET['Image']:
        search_term = request.GET.get('Image')
        searched_photo = Photos.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'search.html', {"message":message, "Image":searched_photo})
    else:
        message = 'You haven\'t searched for any photos.'
        return render(request, 'search.html', {"message":message})