from django.shortcuts import render
from placesapp.models import Place
from django.views import generic
# Create your views here.
def index(request):
    num = Place.objects.all().count()
    context = {'num': num}
    return render(request, 'index.html', context=context)

class PlacesListView(generic.ListView):
    model = Place

class PlaceDetailView(generic.DetailView):
    model = Place

def all_cities(request):
    place = Place.objects.distinct('city')
    return render(request, 'placesapp/all_cities.html', context={"all_places": place})

def city_places(request,inputcity):
    city = Place.objects.filter(city=inputcity)
    return render(request,'placesapp/city_places.html',context={"cities":city})