from django.db import models

# Create your models here.
class Contact(models.Model):
    # recursive: One To Many relation 
    father = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='bio_father')
    mother = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='bio_sgit mother')

    # recursive: Many To Many relation
    siblings = models.ManyToManyField('self', null=True)

    # recursive: One To One relation
    partner = models.OneToOneField('self', on_delete=models.CASCADE, null=True)

# example
# person1 = Person.objects.create() # mother 
# person2 = Person.objects.create(mother=person1) # child 

# # print 
# person2.mother # get mother 
# person1.mother # get child