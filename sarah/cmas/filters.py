import django_filters 
from . models import *

class OrderFileter(django_filters.FilterSet):
    class Meta:
        model = Entertainment
        exclude = ['address','name','description','link']

class BookFileter(django_filters.FilterSet):
    class Meta:
        model = BookStores
        exclude = ['address','name','description','link']
        
class FoodFileter(django_filters.FilterSet):
    class Meta:
        model = Food
        exclude = ['address','name','description','link']
        
