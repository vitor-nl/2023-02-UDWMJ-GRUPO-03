from django.db import models
from student.models import Student
from professor.models import Professor
from classroom.models import Classroom

# Create your models here.
class Courses(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    duration = models.DurationField()
    student = models.ManyToManyField(Student, related_name='courses')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = 'courses'
        ordering =['id']

    def __str__(self):
        return self.name
