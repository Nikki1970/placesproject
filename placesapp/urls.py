from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listofplaces/',views.PlacesListView.as_view(),name="list-of-places"),
    path('place/<int:pk>/', views.PlaceDetailView.as_view(), name='place-detail'),
]