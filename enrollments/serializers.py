from rest_framework import serializers
from .models import Enrollment

class EnrollmentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.name', read_only=True)
    course_name = serializers.CharField(source='course.name', read_only=True)
    teacher_name = serializers.CharField(source='course.teacher_name.name', read_only=True)
    date = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = [
            'id',
            'student',
            'course',
            'student_name',
            'course_name',
            'teacher_name',
            'date'
        ]

    def get_date(self, obj):
        return obj.enrollment_date.strftime('%d-%m-%Y')
