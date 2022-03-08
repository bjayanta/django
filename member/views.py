from django.shortcuts import render
from django.views.generic import View
from .models import *

# Create your views here.

class Home(View):
    def get(self, request, *args, **kwargs):
        context = {}
        person = Person.objects.get(id=3)

        context['person'] = person
        context['interests'] = person.interests.all()

        return render(request, "member/home.html", context)
