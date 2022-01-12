from django.shortcuts import render
from cmas.models import *
from .filters import *
# Create your views here.
def index(request):
    facts =  DC_facts.objects.order_by('?').first()
    return render(request,'cmas/home.html',context={'fact':facts})

def stuff(request):
    ent = Entertainment.objects.all()
    myFil = OrderFileter(request.GET,queryset=ent)
    ent = myFil.qs
    context = {'ent':ent,'fil':myFil}
    return render(request,'cmas/e.html',context)
def books(request):
    ent = BookStores.objects.all()
    myFil = BookFileter(request.GET,queryset=ent)
    ent = myFil.qs
    context = {'ent':ent,'fil':myFil}
    return render(request,'cmas/books.html',context)

def food(request):
    ent = Food.objects.all()
    myFil = FoodFileter(request.GET,queryset=ent)
    ent = myFil.qs
    context = {'ent':ent,'fil':myFil}
    return render(request,'cmas/food.html',context)
def kitties(request):
    return render(request,'cmas/kitties.html')