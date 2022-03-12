from doctest import Example
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Person(models.Model):
    mother = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='children')
    siblings = models.ManyToManyField('self')
    partner = models.OneToOneField('self', on_delete=models.CASCADE, null=True, related_name='husband_and_wife')

# person1 = Person.objects.create()
# person2 = Person.objects.create(mother=person1)

# person2.mother
# person1.children 

# custom validation
def int_is_even(value):
    if (value % 2 != 0):
        raise ValidationError(str(value) + " is not even")

# custom field
class EventInteger(models.IntegerField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.validators.add(int_is_odd)
        self.validators.append(int_is_even)

class MyModel(models.Model):
    # even_int = models.IntegerField(validators=[int_is_even]) # implement validation rule 
    even_int = EventInteger() # implement validation rule 

# Example 
'''
from contact.models import MyModel
odd = MyModel.objects.create(even_int=1)
odd.full_clean()
'''

