from django.db import models

# Create your models here.
class Person(models.Model):
    mother = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='children')
    siblings = models.ManyToManyField('self', null=True, related_name='brother_and_sister')
    partner = models.OneToOneField('self', on_delete=models.CASCADE, null=True, related_name='husband_and_wife')

# person1 = Person.objects.create()
# person2 = Person.objects.create(mother=person1)

# person2.mother
# person1.children