
from django.db import models
from teachers.models import Teacher

class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher_name = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.name
