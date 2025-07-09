from rest_framework import viewsets
from .models import Teacher
from .serializers import  TeacherSerializer
from rest_framework.permissions import IsAuthenticated
class TeacherViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
