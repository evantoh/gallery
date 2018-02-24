
from django .shortcuts import render
from .models import Image 
from django.http import HttpResponse,Http404


# Create your views here.
def welcome(request):
    #get objects from the databasei.e from class image
    images =Image.objects.all()
    #pass the objects to view
    return render(request,'photos/welcome.html',{ "images":images})

def search_results(request):
    
    if 'photos' in request.GET and request.GET["photos"]:
        search_term = request.GET.get("photos")
        searched_photos = Image.search_by_category(search_term)
        message = f"{search_term}"
        return render(request, 'photos/search.html', {"message":message,"photos":searched_photos})

    else:
        message = "You haven't searched for any photos"
        return render(request, 'photos/search.html', {"message":message})
# a function that get data from db of a specific id
def single_photo(request,image_id):
    photo=Image.objects.get(id=image_id)
    return render(request,"photos/single_photo.html",{"photo":photo})