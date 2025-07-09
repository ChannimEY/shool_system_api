from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(
    max_length=10,
    choices=[("female", "Female"), ("male", "Male")]
)

    age= models.IntegerField()

    def __str__(self):
        return self.name
