from django.db import models

# Create your models here.
class Interest(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class City(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Person(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20)
    interests = models.ManyToManyField(Interest)

    def __str__(self):
        return self.name

class PersonAddress(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=200)

    def __str__(self):
        return self.person.name + "(" + self.street_address + ")"
    
