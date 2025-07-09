from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated
class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
