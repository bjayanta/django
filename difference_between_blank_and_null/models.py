from django.db import models

# Create your models here.
class Dean(models.Model):
    int_value = models.IntegerField(null=True, blank=True)
    str_value = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return 'Int is {}, Str is {}'.format(self.int_value, self.str_value)

'''
"null" option is related to database table 
"blank" option is related to front-end form(interface)
'''