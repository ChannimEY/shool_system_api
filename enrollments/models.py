from django.db import models

class Enrollment(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.name} on {self.enrollment_date}"
