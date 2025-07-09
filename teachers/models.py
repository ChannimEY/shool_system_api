from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=10,
        choices=[("female", "Female"), ("male", "Male")]
    )
    phone = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name
