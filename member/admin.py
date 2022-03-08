from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register([Interest, City, Person, PersonAddress])

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile',)

@admin.register(PersonAddress)
class PersonAddressAdmin(admin.ModelAdmin):
    list_display = ('person', 'city', 'street_address',)