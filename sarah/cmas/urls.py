from django.urls import path
from cmas import views

urlpatterns = [
    path('', views.index,name='home'), 
    path('stuff/',views.stuff,name='stuff'),
    path('books/',views.books,name='books'),
    path('food/',views.food,name='food'),
    path('kitties/',views.kitties,name='kitties'),
]