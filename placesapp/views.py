from django.shortcuts import render
from placesapp.models import Place

# Create your views here.
def index(request):
    num = Place.objects.all().count()
    context = {'num': num}
    return render(request, 'index.html', context=context)

