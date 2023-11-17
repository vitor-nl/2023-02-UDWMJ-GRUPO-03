from django.db import models
from person.models import Person

# Create your models here.

class Professor(Person):
    specialty = models.fields.CharField('specialty', max_length=50)
    
    class Meta:
        verbose_name_plural = 'Professors'
        ordering =['id']

    def __str__(self):
        return self.name
