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
