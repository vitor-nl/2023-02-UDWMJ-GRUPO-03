from django.db import models
from person.models import Person

# Create your models here.
class Student(Person):

    class Meta:
        verbose_name_plural='students'
        ordering=['id']

    def __str__(self):
        return self.name