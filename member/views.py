from django.shortcuts import render, HttpResponse 
from django.views.generic import View 
from .models import *

# Create your views here.

class Home(View):
    def get(self, request, *args, **kwargs):
        context = {}
        person = Person.objects.get(id=3)

        context['person'] = person
        context['interests'] = person.interests.all() # forward relationship 
        context['address'] = person.personaddress
        context['all_interests'] = Interest.objects.all()

        city = City.objects.all()
        context['cities'] = city

        return render(request, "member/home.html", context)

class Incity(View):
    def get(self, request, *args, **kwargs):
        context = {}
        id = kwargs.get('id', 1)

        city = City.objects.get(id=id)

        context['city'] = city
        context['all_person_address'] = city.personaddress_set.all() # reverse relationship 

        return render(request, "member/incity.html", context)

class Ininterest(View):
    def get(self, request, *args, **kwargs):
        context = {}
        id = kwargs.get('id', 1)

        interest = Interest.objects.get(id=id)

        context['interest'] = interest
        context['all_person'] = interest.person_set.all() # reverse relationship 

        return render(request, "member/ininterest.html", context)
