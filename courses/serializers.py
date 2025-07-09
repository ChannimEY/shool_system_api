
from rest_framework import serializers
from .models import Course
from teachers.models import Teacher

class CourseSerializer(serializers.ModelSerializer):
    teacher_name = serializers.SerializerMethodField()
    teacher = serializers.PrimaryKeyRelatedField(source='teacher_name', queryset=Teacher.objects.all(), write_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'teacher', 'teacher_name']

    def get_teacher_name(self, obj):
        return str(obj.teacher_name)
