from django.db import models

# Create your models here.
GENDER_CHOISES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

class User(models.Model):
    email = models.CharField(max_length=100, primary_key=True, unique=True)
    first_name = models.CharField("Your first name", max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, default='Doe', verbose_name="Your last name")
    gender = models.CharField(max_length=1, choices=GENDER_CHOISES, null=True)

"""
Table is: 
-----------------
models_guide_user

Fields:
-------------------
id
first_name
last_name

Example:
-----------------------
User(first_name="", lase_name="", gender="")
"""